from static.Types.SystemType import *
from static.Types.ObjectType import *
from static.Types.PanelType import *

from starsystems.models import *


def get_sql_system(f_name: str) -> SystemClass:
    return 1


def get_sql_system_pair():
    return 1


def get_sql_object(f_id: int) -> ObjectClass:
    return 1


def get_sql_panel(f_id: int) -> BasePanel:    
    row = Panels.objects.get(pk = f_id)
    l_div_id = row.div_id
    l_type_id = row.type
    l_values_id = row.values
    l_is_slider = False if l_values_id.is_slider == "False" else True
    
    match l_type_id.id:
        case 1:
            n_panel = SimpleMusicSlider(l_div_id, l_values_id.img_src, [l_values_id.color_a, l_values_id.color_b, l_values_id.b])
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            n_panel = TopHeaderTextPanel(l_div_id, l_values_id.title, l_values_id.text, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], [l_values_id.h_color_a, l_values_id.h_color_b], l_is_slider)
        case 9:
            pass
        case _:
            n_panel = BasePanel("_NONE_")
    return n_panel
