
import os
import logging
import jinja2
import inspect
import imp
from glob import glob

log = logging.getLogger('apydoc')


def basepath() -> str:
    dirname = os.path.dirname(os.path.abspath(__file__))
    return dirname


def process_directory(path: str, modname: str=None) -> dict:
    modules = dict()
    for (dirpath, _, filenames) in os.walk(path):
        mpath = get_module_path(path, modname)
        for filename in [f for f in filenames if f.endswith('.py') and not f == '__init__.py']:
            fname = filename.split('.')[0]
            if mpath:
                name = mpath + '.' + fname
            else:
                name = fname

            path = os.path.join(dirpath, filename)
            modules[name] = process_file(path)

    return modules

        
def get_module_path(path: str, basemod: str=None) -> str:
    if basemod:
        path = path.replace('.', basemod)
    else:
        path = path.replace('./', '')
        path = path.replace('.', '')

    path = path.replace('/', '.')

    return path


def process_file(path: str) -> dict:

    filename = os.path.basename(path)
    name = filename.split('.')[0]
    mod = imp.load_source(name, path)

    out = dict()
    out['name'] = name
    out['filename'] = filename
    out['doc'] = inspect.getdoc(mod)
    out['functions'] = get_functions(mod, name)
    out['classes'] = get_classes(mod, name)

    return out


def process_module(modname: str) -> dict:
    try:
        mod = __import__(modname)
    except Exception:
        log.error('Unable to import module %s', modname)
        return

    out = dict()
    out['name'] = modname
    out['filename'] = mod.__file__
    out['doc'] = inspect.getdoc(mod)
    out['functions'] = get_functions(mod, modname)
    out['classes'] = get_classes(mod, modname)
    return out


def get_classes(obj: object, module: str=None) -> list:
    """Get lisf ot classes of the given object, each class is represented
    by dictionary with fields: name, doc and functions, where function is
    list of functions given by get_function
    """
    out = list()
    for cl in inspect.getmembers(obj, inspect.isclass):
        if cl[0] != "__class__" and not cl[0].startswith("_") and cl[1].__module__ == module:
            log.debug('Class: %s file: %s', cl[0], inspect.getfile(cl[1]))
            outcl = dict()
            outcl['name'] = cl[0]
            outcl['doc'] = inspect.getdoc(cl[1])
            outcl['functions'] = get_functions(cl[1], module)
            out.append(outcl)

    return out


def get_functions(obj: object, module: str=None) -> list:
    """Get list of function of given object, each function is represented
    by dictionary with fields: name, signature and doc.
    """
    out = list()
    for fce in inspect.getmembers(obj, inspect.isfunction):
        if module is None or fce[1].__module__ == module:
            log.debug('Function: %s file: %s', fce[0], inspect.getfile(fce[1]))

            outfce = dict()
            outfce['name'] = fce[0]
            outfce['signature'] = str(inspect.signature(fce[1]))
            outfce['doc'] = inspect.getdoc(fce[1])
            out.append(outfce)

    return out


def load_template(name: str, ttype: str=None) -> (jinja2.Template, str):
    """Load template given by name, or path. If name is given first current
    directory is searched then pyapidoc template directory.
    """

    done = False
    dirname = os.path.dirname(os.path.abspath(__file__))

    if os.path.isdir(name):
        searchpath = os.path.join(name, ttype + '*.jinja')
        log.debug('Looking for template in %s/%s', '.', name)
        paths = glob(searchpath)
        log.debug('Found %s', str(paths))
        if len(paths) == 1:
            path = paths[0]
            if os.path.isfile(path):
                done = True

    if not done:
        searchpath = os.path.join(dirname, 'tpl', name, ttype + '*.jinja')
        log.debug('Looking for template %s', searchpath)
        paths = glob(searchpath)
        log.debug('Found %s', str(paths))
        if len(paths) == 1:
            path = paths[0]
            if os.path.isfile(path):
                done = True

    if not done:
        log.error('Unable to find template %s type %s', name, ttype)
        raise Exception('Unable to find template: {}'.format(name))

    log.debug('Template file path %s', path)
    with open(path) as f:
        template = jinja2.Template(f.read())

    # get desired extension
    filename = os.path.basename(path)
    ext = filename.split('.')[1]

    return template, ext
