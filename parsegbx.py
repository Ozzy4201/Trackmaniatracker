from pygbx import Gbx, GbxType

def parsegbx(file):
    g = Gbx("./ReplayStorage"/file)
    ghost = g.get_class_by_id(GbxType.CTN_GHOST)
    if not ghost:
        quit()
    return[ghost.race_time, ghost.nickname]