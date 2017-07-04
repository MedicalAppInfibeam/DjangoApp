"""Auto-generated file, do not edit by hand. YT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_YT = PhoneMetadata(id='YT', country_code=262, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[268]\\d{8}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='269(?:6[0-4]|50)\\d{4}', example_number='269601234', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='639(?:0[0-79]|1[019]|[26]\\d|3[09]|[45]0|7[06]|9[04-79])\\d{4}', example_number='639012345', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{7}', example_number='801234567', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    leading_digits='269|63')
