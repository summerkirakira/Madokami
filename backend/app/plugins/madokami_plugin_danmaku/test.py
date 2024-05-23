import yt_dlp
import requests
from danmaku_converter import get_video_width_height, get_danmaku_xml


def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'http_headers': {
            'Cookie': "buvid4=AED9FC2E-9BC4-606A-5149-15BDE317200920628-022031214-6e4h6qGA8wPrWuRZYJ1s8w%3D%3D; buvid_fp_plain=undefined; balh_server_inner=__custom__; balh_is_closed=; LIVE_BUVID=AUTO3816480716477231; balh_mode=redirect; buvid3=71FBAD35-00B5-4EBC-8ED7-BE17DBA58FC8167647infoc; DedeUserID=22000392; DedeUserID__ckMd5=889ca05fd9b32810; hit-new-style-dyn=1; CURRENT_BLACKGAP=0; balh_server_custom=https://bilibili.biaoju.site; i-wanna-go-feeds=2; b_nut=100; iflogin_when_web_push=1; enable_web_push=ENABLE; header_theme_version=CLOSE; rpdid=|(k|k)lklkJ|0J'u~|Jku|J)Y; is-2022-channel=1; _uuid=5C74C1066-7A510-10AD7-287D-B10B8BD548EDE09994infoc; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; hit-dyn-v2=1; CURRENT_QUALITY=80; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; SESSDATA=3637672b%2C1731891822%2Cb0e0f%2A52CjDMjY8a_noA_fews8rs542ADiGFWDpChoqIhHIRFmyKp_1HP325gN2Jnz8pguSB3joSVk01N1dMSWxXODR1ajRzSUlOT2dxTGtncld4SXU2YWpBLWM1T0ZyVW9aa0JVS1FPZTk5U1QtQk94aGhXczhuSkRoVExBa0JrTkl1LW1nY1RsdFpHek1nIIEC; bili_jct=66123c6cb3af02e91122a672adc24f16; sid=75fbk883; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY1OTkxMDQsImlhdCI6MTcxNjMzOTg0NCwicGx0IjotMX0.MGhyPXnaKnmgXraV23K0G5OTCgLG7XY7eqKznN6jQrc; bili_ticket_expires=1716599044; share_source_origin=COPY; bp_t_offset_22000392=934382972957622305; home_feed_column=5; browser_resolution=1512-824; bsource=search_google; fingerprint=a5070998673838023da951316fc68fd4; buvid_fp=a5070998673838023da951316fc68fd4; CURRENT_FNVAL=4048; PVID=1; b_lsid=DC25103A4_18FA32F93B9"
        }
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


if __name__ == "__main__":
    info = get_video_info('https://www.bilibili.com/video/BV1xb421q7QB/')
    print(info)