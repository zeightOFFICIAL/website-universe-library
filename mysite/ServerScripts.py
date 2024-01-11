from mysite.Types.SystemType import *
from mysite.Types.ObjectType import *
from mysite.Types.PanelType import *
from mysite.Types.CardType import *
from starsystems.models import *
from operator import attrgetter
from mysite.settings import BASE_DIR


def get_sql_system_id(f_name: str) -> int:
    row = Systems.objects.get(name_name = f_name)
    return row.pk


def get_sql_systems_thumbnail() -> list:
    a_systems = []
    a_row = Systems.objects.all()
    for row in a_row:
        a_systems.append(
            [row.name_name, row.univ_thumbnail_text_url, row.prime_color_any]
        )
    return a_systems


def get_sql_cards() -> list:
    a_cards = []
    a_rows = Systems.objects.all()
    for row in a_rows:
        href = row.name_name.replace(" ", "")
        card = CardClass(
            row.pk,
            row.name_name,
            href,
            row.short_desc_text,
            [row.prime_color_a_plain, row.second_color_a_plain],
            f"{href}cover",
            f"{href.lower()}",
        )
        a_cards.append(card)

    return a_cards


def get_sql_system(f_id: int) -> SystemClass:
    row = Systems.objects.get(pk=f_id)

    l_objects_list = []
    for obj in Objects.objects.all().filter(system=f_id).order_by("orbit_size_int_vmin"):
        l_objects_list.append(get_sql_object(obj.pk))

    l_main_panels_list = []
    for pnl in Panels.objects.all().filter(parent_system=f_id).order_by("div_id_name"):
        l_main_panels_list.append(get_sql_panel(pnl.pk))
    l_main_panels_list.sort(key=attrgetter("id"))

    if not os.path.exists(f"{BASE_DIR}/static/Icons/{row.icon_path_text_url}"):
        row.icon_path_text_url = "AlternativeIcon.ico"

    n_system = SystemClass(
        row.pk,
        row.name_name,
        l_main_panels_list,
        l_objects_list,
        "Icons/" + row.icon_path_text_url,
        [row.prime_color_any, row.second_color_any, row.shadow_color_any],
    )
    return n_system


def get_sql_object(f_id: int) -> ObjectClass:
    row = Objects.objects.get(pk=f_id)
    l_div_id = row.div_id_name
    l_name = row.name_name
    l_type_id = row.type
    l_panels = []
    l_sub_obj = []
    for panel in (
        Panels.objects.all()
        .filter(parent_object=f_id)
        .filter(values__is_slider_bool="False")
    ):
        l_panels.append(get_sql_panel(panel.pk))

    for obj in Objects.objects.all().filter(parent_id=f_id):
        l_sub_obj.append(get_sql_object(obj.pk))

    n_object = ObjectClass(
        l_div_id,
        l_name,
        l_type_id.type_name,
        [
            f"{row.size_int}vh",
            f"-{row.size_int/2}vh",
            row.prime_color_any,
            row.second_color_any,
            row.shadow_power_int_px,
            row.shadow_color_any,
        ],
        [f"{row.orbit_size_int_vmin}vh", f"-{row.orbit_size_int_vmin/2}vh"],
        str(row.orbit_time_int_s),
        l_panels,
        l_sub_obj,
    )

    return n_object


def get_sql_panel(f_id: int) -> BasePanel:
    row = Panels.objects.get(pk=f_id)
    l_div_id = row.div_id_name
    l_type_id = row.type
    l_values_id = row.values
    l_is_slider = True if l_values_id.is_slider_bool == "True" else False
    l_close_button = True if l_values_id.close_button_bool == "True" else False

    n_panel = BasePanel("_NONE_")
    match l_type_id.id:
        case 1:
            n_panel = SimpleMusicSlider(
                l_div_id,
                l_values_id.img_src_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
            )
        case 2:
            needled = []
            for href in l_values_id.extra_args.split(","):
                needled.append(get_sql_panel(int(href)))
            n_panel = PanelSlider(
                l_div_id,
                needled,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
            )
        case 3:
            n_panel = SimpleVideoPanel(
                l_div_id,
                l_values_id.img_src_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
            )
        case 4:
            n_panel = CombinedSimplePanel(
                l_div_id,
                l_values_id.text_plain,
                l_values_id.img_src_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
                l_values_id.layout_int,
                l_is_slider,
            )
        case 5:
            n_panel = SimpleImagePanel(
                l_div_id,
                l_values_id.img_src_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
                l_is_slider,
            )
        case 6:
            n_panel = CombinedHeaderPanel(
                l_div_id,
                l_values_id.title_plain,
                l_values_id.text_plain,
                l_values_id.img_src_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
                [l_values_id.h_color_a_plain, l_values_id.h_color_b_plain],
                l_values_id.layout_int,
                l_is_slider,
            )
        case 7:
            n_panel = HeaderTextPanel(
                l_div_id,
                l_values_id.title_plain,
                l_values_id.text_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
                [l_values_id.h_color_a_plain, l_values_id.h_color_b_plain],
                l_is_slider,
                l_close_button,
                l_values_id.extra_args.split(" "),
            )
        case 8:
            n_panel = TopHeaderTextPanel(
                l_div_id,
                l_values_id.title_plain,
                l_values_id.text_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
                [l_values_id.h_color_a_plain, l_values_id.h_color_b_plain],
                l_is_slider,
            )
        case 9:
            n_panel = SimpleTextPanel(
                l_div_id,
                l_values_id.text_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
                l_is_slider,
            )
        case 11:
            n_panel = SimpleTable(
                l_div_id,
                l_values_id.text_plain,
                [l_values_id.color_a_plain, l_values_id.color_b_plain, l_values_id.color_c_plain],
            )
        case _:
            n_panel
    return n_panel
