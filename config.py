from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "20516665"))
API_HASH = getenv("API_HASH", "9af065cf5fd8ac63600253b19ef6107d")

BOT_TOKEN = getenv("BOT_TOKEN", "6170365487:AAFn1NpmT-v3n_SBO5Lvi-e_SgWC7K4mMSQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5000"))

OWNER_ID = int(getenv("OWNER_ID", "6190680150"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQCnTGmIK05Abp4v71KdsTOjthkcLg_5p5EpWwhJzo_qXeGhk1t6DYNRPDc4fo1ccW6HtqLT18QA1AkLsdLwbYwss4H4PlhH0OyxTOcrYoeXa_4aCZzknlGrU4-iR8S4VabO87nI866bx-0pB_cYbYmXJpO6LVveCzdi6xxRoDit17GucdKzu_61W9Y82cj_zgxhH59qhlxGtqoGsImzXT4IJh_I6_C3atB45YIBf4_VMpQOVINzeFILTvCYlDKQn7shlb2qVTUiLIZ1Of4Rr1Tf8ejwSdHigLXZ4R02XUslp4qi9MxCAZJkT6PHwmMPtMcLUugN066gHAwNsQhU9YDlAAAAAWIpE04A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BlackWorldMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NixaWorld")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6190680150").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
