import random

from .all_tags import *

class Prompter:
    CATEGORY = "promptbymood"
    @classmethod    
    def INPUT_TYPES(s):
        return {
            "required":  {
                "pick_prefix": (["pony","sdxl"], {}),
                "pick_style": (["random","anime","2.5d","real"], {}),
                "w_hcolor_blond": ("INT", {"default": 1}), 
                "w_hcolor_brown": ("INT", {"default": 1}), 
                "w_hcolor_red": ("INT", {"default": 1}), 
                "w_hcolor_black": ("INT", {"default": 1}), 
                "w_hcolor_white": ("INT", {"default": 1}), 
                "w_hcolor_dyed": ("INT", {"default": 1}), 
                "w_bust_small": ("INT", {"default": 1}), 
                "w_bust_medium": ("INT", {"default": 1}), 
                "w_bust_large": ("INT", {"default": 1}), 
                "w_act_solo": ("INT", {"default": 1}), 
                "w_act_vanilla": ("INT", {"default": 1}), 
                "w_act_bdsm": ("INT", {"default": 1}), 
                "w_act_oral": ("INT", {"default": 1}), 
                "w_act_touching": ("INT", {"default": 1}), 
                "w_act_feet": ("INT", {"default": 1}), 
                "w_act_lesbian": ("INT", {"default": 1}), 
                "w_act_extreme": ("INT", {"default": 1}), 
                "w_expression_positive": ("INT", {"default": 1}), 
                "w_expression_neutral": ("INT", {"default": 1}), 
                "w_expression_negative": ("INT", {"default": 1}), 
                "w_expression_sexy": ("INT", {"default": 1}), 
                "w_expression_misc": ("INT", {"default": 1}),
                "w_hstyle_short": ("INT", {"default": 1}), 
                "w_hstyle_long": ("INT", {"default": 1}), 
                "w_hstyle_curly": ("INT", {"default": 1}), 
                "w_hstyle_braided": ("INT", {"default": 1}), 
                "w_hstyle_updo": ("INT", {"default": 1}), 
                "w_hstyle_bangs": ("INT", {"default": 1}), 
                "w_hstyle_ponytail": ("INT", {"default": 1}), 
                "w_addin_shape": ("INT", {"default": 1}), 
                "w_addin_skin": ("INT", {"default": 1}), 
                "w_addin_style": ("INT", {"default": 1}), 
                "w_addin_anthro": ("INT", {"default": 1}), 
                "w_addin_furry": ("INT", {"default": 1}), 
                "w_addin_fantasy": ("INT", {"default": 1}), 
                "w_addin_scifi": ("INT", {"default": 1}), 
                "w_addin_misc": ("INT", {"default": 1}),
                "num_addin": ("INT", {"default": 1}),
                "w_loc_fantasy": ("INT", {"default": 1}), 
                "w_loc_scifi": ("INT", {"default": 1}), 
                "w_loc_contemporary": ("INT", {"default": 2}),
                "w_cloth_topless": ("INT", {"default": 2}),
                "w_cloth_bottomless": ("INT", {"default": 1}),
                "w_cloth_nude": ("INT", {"default": 5}), 
                "w_cloth_full": ("INT", {"default": 1}), 
                "w_cloth_outfit": ("INT", {"default": 1}),
                "seed": ("INT", {"default": 42}),
                }
            }
    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("pos","neg",)
    FUNCTION = "make_prompt"

    def make_prompt(self, seed,
                    pick_prefix, pick_style,
                    w_hcolor_blond, w_hcolor_brown, w_hcolor_red, w_hcolor_black, w_hcolor_white, w_hcolor_dyed,
                    w_bust_small, w_bust_medium, w_bust_large,
                    w_act_solo, w_act_vanilla, w_act_bdsm, w_act_oral, w_act_touching, w_act_feet, w_act_lesbian, w_act_extreme,
                    w_expression_positive, w_expression_neutral, w_expression_negative, w_expression_sexy, w_expression_misc,
                    w_hstyle_short, w_hstyle_long, w_hstyle_curly, w_hstyle_braided, w_hstyle_updo, w_hstyle_bangs, w_hstyle_ponytail,
                    w_addin_shape, w_addin_skin, w_addin_style, w_addin_anthro, w_addin_furry, w_addin_fantasy, w_addin_scifi, w_addin_misc, num_addin,
                    w_loc_fantasy, w_loc_scifi, w_loc_contemporary,
                    w_cloth_topless, w_cloth_bottomless, w_cloth_nude, w_cloth_full, w_cloth_outfit):

        random.seed(seed)



        if pick_style == "random":
            final_style = all_style[random.choice(list(['anime', '2.5d', 'real']))]
        else:
            final_style = pick_style

        # determine hair color
        hair_color_weights = {
            'blond': w_hcolor_blond,
            'brown': w_hcolor_brown,
            'red': w_hcolor_red,
            'black': w_hcolor_black,
            'white': w_hcolor_white,
            'dyed': w_hcolor_dyed}
        final_hair_color = select_random(hair_color_weights, all_hair_color) 
        if final_hair_color: final_hair_color += ' hair'

        # determine bust size
        bust_size_weights = {
            'small': w_bust_small,
            'medium': w_bust_medium,
            'large': w_bust_large
        }
        final_bust_size = select_random(bust_size_weights, all_bust_size)

        # determine act
        act_weights = {
            'solo': w_act_solo,
            'vanilla': w_act_vanilla,
            'bdsm': w_act_bdsm,
            'oral': w_act_oral,
            'touching': w_act_touching,
            'feet': w_act_feet,
            'lesbian': w_act_lesbian,
            'extreme': w_act_extreme
        }
        final_act = select_random(act_weights, all_act)

        # determine expression
        expression_weights = {
            'positive': w_expression_positive,
            'neutral': w_expression_neutral,
            'negative': w_expression_negative,
            'sexy': w_expression_sexy,
            'misc': w_expression_misc
        }
        final_expression = select_random(expression_weights, all_expression)

        # determine hair style
        hair_style_weights = {
            'short': w_hstyle_short,
            'long': w_hstyle_long,
            'curly': w_hstyle_curly,
            'braided': w_hstyle_braided,
            'updo': w_hstyle_updo,
            'bangs': w_hstyle_bangs,
            'ponytail': w_hstyle_ponytail
        }
        final_hair_style = select_random(hair_style_weights, all_hair_style)

        # add the number of addins specified
        final_addins = []
        for _ in range(num_addin):

            # determine addin
            addin_weights = {
                'shape': w_addin_shape,
                'skin': w_addin_skin,
                'style': w_addin_style,
                'anthro': w_addin_anthro,
                'furry': w_addin_furry,
                'fantasy': w_addin_fantasy,
                'scifi': w_addin_scifi,
                'misc': w_addin_misc
            }
            final_addins.append(select_random(addin_weights, all_addin))

        # determine locale
        loc_weights = {
            'fantasy': w_loc_fantasy,
            'scifi': w_loc_scifi,
            'contemporary': w_loc_contemporary,
        }
        final_loc = select_random(loc_weights, all_loc)

        # determine clothing
        choices = elim_empty(
            {
                "topless": w_cloth_topless,
                "bottomless": w_cloth_bottomless,
                "nude": w_cloth_nude,
                "full": w_cloth_full,
                "fit": w_cloth_outfit
            }
        )
        final_type_cloth = weighted_choice(choices)

        if final_type_cloth:

            final_cloth = ''

            if final_type_cloth == "nude":
                final_cloth = "nude"
            
            if final_type_cloth in ["topless", "full"]:
                final_cloth += random.choice(list(all_bottom))

            if final_type_cloth == "full":
                final_cloth += ', '

            if final_type_cloth in ["bottomless", "full"]:
                final_cloth += random.choice(list(all_top))

            if final_type_cloth == "fit":
                final_cloth = random.choice(list(all_fit))

        else:
            final_cloth = None

        final_prompt = ""

        # these two must exist
        final_prompt += all_prompt_prefix[pick_prefix]
        final_prompt += ',' + final_style

        # the rest might be skipped
        if final_act: final_prompt += ',' + final_act
        if final_expression: final_prompt += ',' + final_expression
        if final_bust_size: final_prompt += ',' + final_bust_size
        if final_hair_color: final_prompt += ',' + final_hair_color
        if final_hair_style: final_prompt += ',' + final_hair_style
        for addin in final_addins:
            if addin: final_prompt += ',' + addin
        if final_cloth: final_prompt += ',' + final_cloth
        if final_loc: final_prompt += ',' + final_loc

        return (final_prompt,neg_prompt_prefix[pick_prefix],)

def weighted_choice(choices):

    total = 0
    for k in choices: total += choices[k]

    r = random.uniform(0, total)
    upto = 0
    for k in choices:
        w = choices[k]
        if upto + w >= r:
            return k
        upto += w

    assert False

def elim_empty(weights):

    choices = {}
    for k in weights:
        if weights[k] > 0:
            choices[k] = weights[k]
    return choices

def select_random(weights, all_list):

    # if all weights are zero, then this is not considered
    zero_check = 0
    for k in weights: zero_check += weights[k]
    if zero_check == 0: return None

    choices = elim_empty(weights)

    final_category = weighted_choice(choices)
    final_category = all_list[final_category]
    return random.choice(list(final_category))