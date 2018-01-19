# mpythonrun -f /usr/ghs/int1144/modules/renesas/scripts/integrity.py
# execfile("/usr/ghs/int1144/modules/renesas/scripts/integrity.py")

#DEFINE ENVIRONMENT



OS_DIR='/usr/ghs/int1144/'
BSP_NAME='simarm/'
BSP_DIR=OS_DIR + BSP_NAME
BUILD_DIR=OS_DIR + 'bin/' + BSP_NAME

top_project = 'default.gpj'
target_projet = 'kernel'
def open_default_project():
    Prj_mng = GHS_ProjectManager()
    print('Open defaul project: '+BSP_DIR + top_project)
    pmw = Prj_mng.OpenProject(BSP_DIR + top_project) 
    top_project_dir = w.getinput('kdjkd', ['dfd'], False, "input BSP dir: ")
    return pmw

def build_project(project_name,clean=False):
    pmw = open_default_project()
    #pmw.find(target_projet+'.gpj')
    if clean == True:
        pmw.Build(project_name + ' --cleanfirst')
    else:
        pmw.Build(project_name)
    pmw.CloseWin()
    return None

def debug_prj(project_name,connection_name = 'isimmarm'):
    dw = GHS_Debugger().debug(BUILD_DIR + project_name)
    fm = dw.connect(connection_name)
    dw.RunCmd("set_runmode_partner -auto")
    dw.run()
    dw.RunCmd("wait -runmode_partner")
    return dw,fm

def load_module(connection, module_name):
    connection.load(module_name)

if __name__ == "__main__":

    prj_kernel = 'kernel'

    build_project(prj_kernel)

    debug_wm,connection = debug_prj(prj_kernel)


    load_target = 'helloworld2'

    build_project(load_target,clean=True)
    load_module(connection, load_target)
    debug_wm.RunCmd("wait -taskStatus Created -addressSpace "+ load_target +" -taskName Initial");
    debug_wm.RunCmd("route runmode target r " + load_target)
    #dw.Runcmd('quit force')
