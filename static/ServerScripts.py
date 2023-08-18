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
    l_is_slider = True if l_values_id.is_slider == "True" else False
    
    n_panel = BasePanel("_NONE_")
    match l_type_id.id:
        case 1:
            n_panel = SimpleMusicSlider(l_div_id, l_values_id.img_src, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c])
        case 2:
            pass
        case 3:
            n_panel = SimpleVideoPanel(l_div_id, l_values_id.img_src, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c])
        case 4:
            n_panel = CombinedSimplePanel(l_div_id, l_values_id.text, l_values_id.img_src, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], l_values_id.layout, l_is_slider)
        case 5:
            n_panel = SimpleImagePanel(l_div_id, l_values_id.img_src, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], l_is_slider)
        case 6:
            n_panel = CombinedHeaderPanel(l_div_id, l_values_id.title, l_values_id.text, l_values_id.img_src, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], [l_values_id.h_color_a, l_values_id.h_color_b], l_values_id.layout, l_is_slider)
        case 7:
            n_panel = HeaderTextPanel(l_div_id, l_values_id.title, l_values_id.text, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], [l_values_id.h_color_a, l_values_id.h_color_b], l_is_slider, l_values_id.close_button, l_values_id.extra_hrefs)
        case 8:
            n_panel = TopHeaderTextPanel(l_div_id, l_values_id.title, l_values_id.text, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], [l_values_id.h_color_a, l_values_id.h_color_b], l_is_slider)
        case 9:
            n_panel = SimpleTextPanel(l_div_id, l_values_id.text, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], l_is_slider)
        case _:
            n_panel = BasePanel("_NONE_")
    return n_panel
