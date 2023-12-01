import json
from time import sleep

import instaloader
from instaloader import *
import requests


url = "https://i.instagram.com/api/v1/accounts/login/"

headers = {
    "Host": "i.instagram.com",
    "X-Ig-App-Locale": "ar_EG",
    "X-Ig-Device-Locale": "ar_EG",
    "X-Ig-Mapped-Locale": "ar_AR",
    "X-Pigeon-Rawclienttime": "1701358983.724",
    "X-Ig-Bandwidth-Speed-Kbps": "49678.000",
    "X-Ig-Bandwidth-Totalbytes-B": "9884236",
    "X-Ig-Bandwidth-Totaltime-Ms": "199",
    "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
    "X-Ig-Www-Claim": "0",
    "X-Bloks-Is-Layout-Rtl": "true",
    "X-Ig-Device-Id": "ea773184-7663-4e32-8c38-c8180cf5827f",
    "X-Ig-Family-Device-Id": "ac7f2c7c-04f1-4452-b9f1-938c345e3471",
    "X-Ig-Android-Id": "android-fe2ca0b5d8b6ce3c",
    "X-Ig-Timezone-Offset": "28800",
    "X-Ig-Nav-Chain": "SelfFragment:self_profile:1:cold_start:1701358939.925::,ProfileMediaTabFragment:self_profile:2:button:1701358941.92::,ProfileMenuFragment:bottom_sheet_profile:3:button:1701358946.971::,ProfileMenuFragment:bottom_sheet_profile:4:button:1701358946.973::,ProfileMediaTabFragment:self_profile:5:button:1701358949.755::,AccountSwitchFragment:account_switch_fragment:6:button:1701358950.937::,AddAccountBottomSheetFragment:add_account_bottom_sheet:7:button:1701358954.268::,LoginLandingFragment:login_landing:8:button:1701358965.229::",
    "X-Ig-Client-Endpoint": "login_landing",
    "X-Fb-Connection-Type": "WIFI",
    "X-Ig-Connection-Type": "WIFI",
    "X-Ig-Capabilities": "3brTv10=",
    "Priority": "u=3",
    "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; google; G011A; G011A; intel; ar_EG; 458229258)",
    "Accept-Language": "ar-EG, en-US",
    "Ig-Intended-User-Id": "0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Length": "466",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Fb-Http-Engine": "Liger",
    "X-Fb-Client-Ip": "True",
    "X-Fb-Server-Cluster": "True",
    "two_factor_required": "true"  # إضافة خاصية التوثيق الثنائي
}
r="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡷⡀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠺⣟⡽⠀⠀⠀⠀⠀⠀⠀⠈⠑⠂⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠊⠁⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠈⠳⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠆⠀⢰⡃⠀⠐⡄⠀⢲⠀⠃⢻⠀⠀⠀⡄⠀⠀⠈⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣶⣄⣺⢇⡄⠀⡇⠀⢰⢺⠱⣄⠀⠘⢆⠈⡆⠀⠸⠀⠀⠀⡇⠀⠀⠀⠰⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⡏⢸⠀⠀⡇⠀⢸⣾⢀⣨⣷⡄⠈⢣⣇⠀⠀⡆⠀⠀⡇⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⢸⡄⢸⡇⡀⢸⢿⡏⠀⣀⣹⣦⡀⢿⠀⠀⡇⠀⠀⡇⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⡄⠈⡇⠈⣿⣿⣼⣞⣷⠾⣿⣿⡿⠉⢻⠀⠀⡇⠀⠀⡿⠟⢷⡄⠀⠀⠀⡘⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⣇⢸⢿⡀⠇⠻⠉⠸⠏⣠⠟⠉⠀⠀⠀⡄⠀⠿⠀⠀⣿⡀⠀⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣾⣷⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢀⡿⢃⣼⠁⠀⠀⠃⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⡻⢯⣻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⢸⡧⡎⢸⠃⠀⠀⢠⢀⣸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⢸⠉⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⡇⡇⢸⠀⠀⠀⢸⡈⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⢸⡀⠀⠀⠀⢀⡠⠴⠚⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⡇⢸⢸⡀⠀⠀⠈⡇⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡆⠀⢇⠀⠀⠰⠋⠀⠀⠀⠀⠀⠀⠀⠀⢨⠀⠀⠀⢸⠃⠈⡇⡇⠀⠀⠀⢱⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠍⠀⠀⠀⣿⠀⠀⢡⠱⠀⠀⠀⠸⡜⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣽⢆⠀⠀⠀⠀⠀⣠⠒⠁⠉⢀⡆⠀⠀⣿⡄⠀⠸⡄⠀⠀⠀⠀⢇⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⣿⠀⠓⠤⠔⠒⠻⡇⢀⡴⠚⠉⡇⠀⠀⡧⢇⠀⠀⢱⡀⠀⠀⠀⠘⣾⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡆⠀⢰⣿⡄⡆⠀⠀⠀⠀⢷⠋⠀⠀⠀⡇⠀⢀⠁⢈⠷⢶⣤⡷⣤⣤⢤⡤⠞⠓⠒⠦⢄⡀⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⡇⡇⢁⠀⠀⠀⢀⢻⠀⠀⠀⠀⡇⠀⢸⠀⠣⢤⣀⣞⡏⠉⡱⠋⠀⠀⠀⠀⠀⠀⠙⡆
⠀⠀⠀⠀⠀⠀⢸⠀⠀⡞⠀⢡⢸⡀⠀⣀⡼⠀⢳⠀⠀⠀⡇⠀⡏⠀⢀⣾⣿⣾⣟⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻
⠀⠀⠀⠀⠀⠀⢸⠀⢠⠇⠀⠈⢇⡷⣺⢿⠏⡞⠑⠚⠉⢀⠀⢠⠁⣠⣿⣿⣻⣟⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿
⠀⠀⠀⠀⠀⠀⣿⠀⡘⢀⣠⠞⣉⠵⣡⠏⠀⢧⠀⠀⠀⣸⠀⣾⣼⣉⣉⣍⡿⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⢀⣴⡿⢠⠏⣉⣵⠞⠁⡰⡃⠀⠀⢘⡤⠴⢒⠇⢠⣿⡀⣉⣴⣿⣿⡁⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹
⠀⠀⠀⢀⠎⢸⡇⣸⣾⣿⣿⣀⣴⢱⣇⡤⠚⠁⢀⠀⣼⠄⡿⠋⠉⠁⢸⡛⢿⠑⢤⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⡞⢀⣎⢧⣟⣿⡿⠋⠀⠀⠉⠁⠀⣠⣾⠟⣸⡟⢸⠁⠀⠀⠀⠸⡇⢸⡄⢸⠃⠀⢀⣠⠤⠤⠤⠔⠢⡀⣸
⠀⠀⣸⠀⡸⢸⡟⣶⡿⠁⠀⠀⠀⠀⠀⠀⠉⠀⢠⣿⠀⡞⠀⠀⠀⠀⡇⣿⠸⣿⣾⠀⠀⠀⠙⠒⠒⠲⣌⣠⢌⣻
⠀⠀⡏⠀⣇⠞⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢿⢻⠀⡇⠀⠀⠀⠀⣷⡇⠀⢻⢹⡄⠀⠀⠀⠀⠀⠀⠈⠁⠀⣼
⠀⢰⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⣞⡄⡇⠀⠀⠀⠀⡿⡇⠀⠸⡆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟
⠀⡞⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⠀⢸⢸⠛⠙⠻⠀⠀⠀⠀⢣⡇⠀⠀⡇⢡⠀⠀⠀⠀⠀⡀⠀⠀⠀⡇
⠀⢳⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡿⠀⠀⡞⡀⠀⠀⠀⠀⠀⠀⠘⡾⡄⠀⡇⢸⠀⠀⠀⠀⡼⠁⠀⠀⢠⠃
⢸⢸⠀⣾⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠘⣿⣆⡇⡆⠀⠀⣀⡜⠁⠀⠀⠀⢸⡆⠀⠀⠀
"""

print(f"\u001b[31m{r}\u001b[0m")
us=input("user: ")
ps=input("pass: ")
arabic_text = "كود المنشور يكون بهذا الشكل"
arabic_url = "https://www.instagram.com/C0SBieHggMm/?igshid=NTc4MTIwNjQ2YQ=="
arabic_info = "نقوم باخذ C0SBieHggMm فقط"

english_text = "The post code should be in this format"
english_url = "https://www.instagram.com/C0SBieHggMm/?igshid=NTc4MTIwNjQ2YQ=="
english_info = "We only take C0SBieHggMm"

#تنسيق النصوص وإضافة الألوان
formatted_arabic = '\033[92m{}\033[0m\n\033[92m{}\033[0m\n{}'.format(arabic_text, arabic_url, arabic_info)
formatted_english = '\033[92m{}\033[0m\n\033[92m{}\033[0m\n{}'.format(english_text, english_url, english_info)

# طباعة النصوص المنسقة
print(formatted_arabic)
print(formatted_english)
code_post=input("Enter Code: ")
data = {
    "signed_body": "SIGNATURE.{\"jazoest\":\"22327\",\"country_codes\":\"[{\\\"country_code\\\":\\\"\\\",\\\"source\\\":[\\\"sim\\\"]},{\\\"country_code\\\":\\\"20\\\",\\\"source\\\":[\\\"default\\\"]}]\",\"phone_id\":\"ac7f2c7c-04f1-4452-b9f1-938c345e3471\",\"enc_password\":\"#PWD_INSTAGRAM:0:1701358983:بببببب\",\"username\":\"ييييييي\",\"adid\":\"76bd4ebd-7bd0-4428-9545-90ee00a1d626\",\"guid\":\"ea773184-7663-4e32-8c38-c8180cf5827f\",\"device_id\":\"android-fe2ca0b5d8b6ce3c\",\"google_tokens\":\"[]\",\"login_attempt_count\":\"0\"}".replace("بببببب",ps).replace("ييييييي",us)
}



response = requests.post(url, headers=headers, data=data)
response_headers = response.headers



data_login= response.text
data_json = json.loads(data_login)
pk = data_json["logged_in_user"]["pk"]
fbid_v2 = data_json["logged_in_user"]["fbid_v2"]
profile_pic_id = data_json["logged_in_user"]["profile_pic_id"]
interop_messaging_user_fbid = data_json["logged_in_user"]["interop_messaging_user_fbid"]
strong_id__ = data_json["logged_in_user"]["strong_id__"]
session_flush_nonce = data_json["session_flush_nonce"]
if response.status_code== 200:

    print("Login succeeded")
    print("pk:", pk)
    print("fbid_v2:", fbid_v2)
    print("profile_pic_id:", profile_pic_id)
    print("interop_messaging_user_fbid:", interop_messaging_user_fbid)
    print("strong_id__:", strong_id__)
    print("session_flush_nonce:", session_flush_nonce)

    ig_set_authorization = response_headers.get("ig-set-authorization")
    x_ig_set_www_claim = response_headers.get("x-ig-set-www-claim")
    content_security_policy = response_headers.get("content-security-policy")
    report_to = response_headers.get("report-to")
    x_fb_client_ip_forwarded = response_headers.get("X-FB-Client-IP-Forwarded")
    Ig_U_Rur = response_headers.get("g-Set-Ig-U-Rur")
    X_Pigeon_Session_Id = response_headers.get("X-Pigeon-Session-Id")

    print("ig-set-authorization: " + str(ig_set_authorization))
    print("x-ig-set-www-claim: " + str(x_ig_set_www_claim))
    print("content-security-policy: " + str(content_security_policy))
    print("report-to: " + str(report_to))
    print("X-FB-Client-IP-Forwarded: " + str(x_fb_client_ip_forwarded))
    print("X_Pigeon_Session_Id: " + str(X_Pigeon_Session_Id))
else:
    print(f"Login failed : {response.status_code}")



loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, us)
user_id = profile.userid


def get_id(username):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        "X-IG-App-ID": "936619743392459"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    user_id = data["data"]["user"]["id"]
    return user_id


def get_id_store(id_so):

    url = f"https://i.instagram.com/api/v1/feed/user/{id_so}/story/?supported_capabilities_new=[{{\"name\":\"SUPPORTED_SDK_VERSIONS\",\"value\":\"\"}},{{\"name\":\"FACE_TRACKER_VERSION\",\"value\":\"14\"}},{{\"name\":\"segmentation\",\"value\":\"segmentation_enabled\"}},{{\"name\":\"COMPRESSION\",\"value\":\"ETC2_COMPRESSION\"}},{{\"name\":\"world_tracker\",\"value\":\"world_tracker_enabled\"}},{{\"name\":\"gyroscope\",\"value\":\"gyroscope_enabled\"}}]"
    headers = {
        "Host": "i.instagram.com",
        "X-Ig-App-Locale": "ar_EG",
        "X-Ig-Device-Locale": "ar_EG",
        "X-Ig-Mapped-Locale": "ar_AR",
        "X-Pigeon-Session-Id": "UFS-84ea4893-3dc1-480a-95f6-7ebb4229becd-2",
        "X-Pigeon-Rawclienttime": "1701364800.830",
        "X-Ig-Bandwidth-Speed-Kbps": "49678.000",
        "X-Ig-Bandwidth-Totalbytes-B": "9884236",
        "X-Ig-Bandwidth-Totaltime-Ms": "199",
        "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
        "X-Ig-Www-Claim": f"{x_ig_set_www_claim}",
        "X-Bloks-Is-Layout-Rtl": "true",
        "X-Ig-Device-Id": "ea773184-7663-4e32-8c38-c8180cf5827f",
        "X-Ig-Family-Device-Id": "ac7f2c7c-04f1-4452-b9f1-938c345e3471",
        "X-Ig-Android-Id": "android-fe2ca0b5d8b6ce3c",
        "X-Ig-Timezone-Offset": "28800",
        "X-Ig-Nav-Chain": "MainFeedFragment:feed_timeline:1:cold_start:1701364131.472:10#230#301:3247466269753376457,UserDetailFragment:profile:2:media_owner:1701364559.959::,ProfileMediaTabFragment:profile:3:button:1701364561.150::",
        "X-Ig-Client-Endpoint": "ProfileMediaTabFragment:profile",
        "X-Fb-Connection-Type": "WIFI",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-App-Id": "567067343352427",
        "Priority": "u=3",
        "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; google; G011A; G011A; intel; ar_EG; 458229258)",
        "Accept-Language": "ar-EG, en-US",
        "Authorization": f"{ig_set_authorization}",
        "X-Mid": "ZWgqzwABAAHT7eCuQl36RXbLcF7V",
        "Ig-U-Ds-User-Id": f"{user_id}",
        "Ig-U-Rur": f"{Ig_U_Rur}",
        "Ig-Intended-User-Id": f"{user_id}",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Fb-Http-Engine": "Liger",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Server-Cluster": "True"
    }

    responses = requests.get(url, headers=headers)
    def get_strong_id_values(response):
        data = json.loads(response)
        values = []

        def find_values(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key == "strong_id__" and "_" in value:
                        values.append(value)
                    elif isinstance(value, (dict, list)):
                        find_values(value)
            elif isinstance(obj, list):
                for item in obj:
                    find_values(item)

        find_values(data)
        return values
    oooo = get_strong_id_values(responses.text)

    return oooo

def get_id_post():
    L = instaloader.Instaloader()
    post_shortcode = code_post
    media_id = Post.shortcode_to_mediaid(post_shortcode)
    return media_id
def req_Grt_user():
    idd=get_id_post()
    print(171 & idd)
    url = f'https://i.instagram.com/api/v1/media/{idd}/likers/'

    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'ar_EG',
        'X-Ig-Device-Locale': 'ar_EG',
        'X-Ig-Mapped-Locale': 'ar_AR',
        'X-Pigeon-Session-Id': 'UFS-ee9e4aa3-e859-4aa8-ac73-d4b788ba4843-0',
        'X-Pigeon-Rawclienttime': '1701384635.781',
        'X-Ig-Bandwidth-Speed-Kbps': '1344.000',
        'X-Ig-Bandwidth-Totalbytes-B': '0',
        'X-Ig-Bandwidth-Totaltime-Ms': '0',
        'X-Bloks-Version-Id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
        "X-Ig-Www-Claim": f"{x_ig_set_www_claim}",
        'X-Bloks-Is-Layout-Rtl': 'true',
        'X-Ig-Device-Id': 'ea773184-7663-4e32-8c38-c8180cf5827f',
        'X-Ig-Family-Device-Id': 'ac7f2c7c-04f1-4452-b9f1-938c345e3471',
        'X-Ig-Android-Id': 'android-fe2ca0b5d8b6ce3c',
        'X-Ig-Timezone-Offset': '28800',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'Priority': 'u=3',
        'User-Agent': 'Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; google; G011A; G011A; intel; ar_EG; 458229258)',
        'Accept-Language': 'ar-EG, en-US',
        "Authorization": f"{ig_set_authorization}",
        'Ig-U-Ig-Direct-Region-Hint': 'RVA,53041017289,1732950013:01f7e2ef546a8b53c2b49e8a1fc04be20ef6d3d66ca1f792df242f5ec445e239f3a36f35',
        'Ig-U-Ds-User-Id': f"{user_id}",
        "Ig-U-Rur": f"{Ig_U_Rur}",
        'Ig-Intended-User-Id': f"{user_id}",
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True'
    }

    response = requests.get(url, headers=headers)

    return response.text

def get_User(response):
    data = json.loads(response)
    users = data["users"]

    usernames = []
    for user in users:
        username = user["username"]
        usernames.append(username)

    with open("usernames.txt", "w") as file:
        for username in usernames:
            file.write(username + "\n")
def send_like(media_id):
    url = "https://i.instagram.com/api/v1/story_interactions/send_story_like/"
    headers = {
        "Host": "i.instagram.com",
        "X-Ig-App-Locale": "ar_EG",
        "X-Ig-Device-Locale": "ar_EG",
        "X-Ig-Mapped-Locale": "ar_AR",
        "X-Pigeon-Session-Id": "UFS-84ea4893-3dc1-480a-95f6-7ebb4229becd-2",
        "X-Pigeon-Rawclienttime": "1701364694.338",
        "X-Ig-Bandwidth-Speed-Kbps": "49678.000",
        "X-Ig-Bandwidth-Totalbytes-B": "9884236",
        "X-Ig-Bandwidth-Totaltime-Ms": "199",
        "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
        "X-Ig-Www-Claim": f"{x_ig_set_www_claim}",
        "X-Bloks-Is-Layout-Rtl": "true",
        "X-Ig-Device-Id": "ea773184-7663-4e32-8c38-c8180cf5827f",
        "X-Ig-Family-Device-Id": "ac7f2c7c-04f1-4452-b9f1-938c345e3471",
        "X-Ig-Android-Id": "android-fe2ca0b5d8b6ce3c",
        "X-Ig-Timezone-Offset": "28800",
        "X-Ig-Nav-Chain": "MainFeedFragment:feed_timeline:1:cold_start:1701364131.472:10#230#301:3247466269753376457,UserDetailFragment:profile:2:media_owner:1701364559.959::,ProfileMediaTabFragment:profile:3:button:1701364561.150::,ReelViewerFragment:stories_viewer:5:button:1701364691.707::",
        "X-Ig-Client-Endpoint": "ReelViewerFragment:reel_profile",
        "X-Fb-Connection-Type": "WIFI",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-App-Id": "567067343352427",
        "Priority": "u=3",
        "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; google; G011A; G011A; intel; ar_EG; 458229258)",
        "Accept-Language": "ar-EG, en-US",
        "Authorization": f"{ig_set_authorization}",
        "X-Mid": "ZWgqzwABAAHT7eCuQl36RXbLcF7V",
        "Ig-U-Ds-User-Id": f"{pk}",
        "Ig-U-Rur": f"{Ig_U_Rur}",
        "Ig-Intended-User-Id": f"{pk}",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length": "285",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Fb-Http-Engine": "Liger",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Server-Cluster": "True"

    }

    data = {
        "signed_body": "SIGNATURE.{\"media_id\":\"" + media_id + "\",\"tray_session_id\":\"f44bc0ac-9400-42e9-8a3d-3862b512380a\",\"_uid\":\"53041017289\",\"_uuid\":\"ea773184-7663-4e32-8c38-c8180cf5827f\",\"viewer_session_id\":\"de990954-7985-4e7e-a4d7-6056c1640375\",\"container_module\":\"reel_profile\"}"
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code ==200:
        print('Send Like!')
    else:
        print("Er")
    return response.status_code




usernames_list = []






if response.status_code == 200:
    id_post = get_id_post()
    response1 = req_Grt_user()
    print(response1)
    get_User(response1)
    with open('usernames.txt', 'r') as file:
        for line in file:
            username = line.strip()
            usernames_list.append(username)

    print(usernames_list)

    for ittt in usernames_list:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, ittt)
        if profile.is_private:
            print(f"The account @{ittt} is private.")

        else:
            print(f"The account @{ittt} is public.")
            list_id_ators = get_id_store(id_so=get_id(ittt))
            for itme_id in list_id_ators:
                sleep(20)
                status_code = send_like(itme_id)
                send_like(itme_id)
