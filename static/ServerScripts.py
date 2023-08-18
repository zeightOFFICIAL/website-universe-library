from static.Types.SystemType import *
from static.Types.ObjectType import *
from static.Types.PanelType import *
from starsystems.models import *
from operator import attrgetter


def get_sql_system(f_id: int) -> SystemClass:
    row = Systems.objects.get(pk=f_id)
    l_objects_list = []
    for obj in Objects.objects.all().filter(system=f_id):
        l_objects_list.append(get_sql_object(obj.pk))
    l_main_panels_list = []
    for pnl in Panels.objects.all().filter(parent_system=f_id):
        l_main_panels_list.append(get_sql_panel(pnl.pk))
    l_main_panels_list.sort(key=attrgetter('id'))
    n_system = SystemClass(row.pk, row.name, l_main_panels_list, l_objects_list, row.icon_path, [
                           row.prime_color, row.second_color, row.shadow_color])
    return n_system


def get_sql_system_name():
    return 1


def get_sql_system_pair():
    return 1


def get_sql_object(f_id: int) -> ObjectClass:
    row = Objects.objects.get(pk=f_id)
    l_div_id = row.div_id
    l_name = row.name
    l_type_id = row.typename
    l_panels = list[BasePanel]
    panel_row = Panels.objects.all().filter()
    n_object = ObjectClass(l_div_id, l_name, l_type_id.name, [f'{row.size}vh', f'-{row.size/2}vh', row.prime_color, row.second_color,
                           row.shadow_power, row.shadow_color], [f'{row.orbit_size}vh', f'-{row.orbit_size/2}vh'], str(row.orbit_time), [], [])
    return n_object


def get_sql_panel(f_id: int) -> BasePanel:
    row = Panels.objects.get(pk=f_id)
    l_div_id = row.div_id
    l_type_id = row.type
    l_values_id = row.values
    l_is_slider = True if l_values_id.is_slider == "True" else False
    l_close_button = True if l_values_id.close_button == "True" else False

    n_panel = BasePanel("_NONE_")
    match l_type_id.id:
        case 1:
            n_panel = SimpleMusicSlider(l_div_id, l_values_id.img_src, [
                                        l_values_id.color_a, l_values_id.color_b, l_values_id.color_c])
        case 2:
            needled = list[BasePanel]
            for href in l_values_id.extra_hrefs.split(','):
                needled.append(get_sql_panel(href))
            n_panel = PanelSlider(l_div_id, needled, [
                                  l_values_id.color_a, l_values_id.color_b, l_values_id.color_c])
        case 3:
            n_panel = SimpleVideoPanel(l_div_id, l_values_id.img_src, [
                                       l_values_id.color_a, l_values_id.color_b, l_values_id.color_c])
        case 4:
            n_panel = CombinedSimplePanel(l_div_id, l_values_id.text, l_values_id.img_src, [
                                          l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], l_values_id.layout, l_is_slider)
        case 5:
            n_panel = SimpleImagePanel(l_div_id, l_values_id.img_src, [
                                       l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], l_is_slider)
        case 6:
            n_panel = CombinedHeaderPanel(l_div_id, l_values_id.title, l_values_id.text, l_values_id.img_src, [
                                          l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], [l_values_id.h_color_a, l_values_id.h_color_b], l_values_id.layout, l_is_slider)
        case 7:
            n_panel = HeaderTextPanel(l_div_id, l_values_id.title, l_values_id.text, [l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], [
                                      l_values_id.h_color_a, l_values_id.h_color_b], l_is_slider, l_close_button, l_values_id.extra_hrefs)
        case 8:
            n_panel = TopHeaderTextPanel(l_div_id, l_values_id.title, l_values_id.text, [
                                         l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], [l_values_id.h_color_a, l_values_id.h_color_b], l_is_slider)
        case 9:
            n_panel = SimpleTextPanel(l_div_id, l_values_id.text, [
                                      l_values_id.color_a, l_values_id.color_b, l_values_id.color_c], l_is_slider)
        case _:
            pass
    return n_panel
