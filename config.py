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

SESSION = getenv("SESSION", "BQBA5Zknkz1h-bSsr8LYQ23lfml7zqR4kXFppHlymMtgEJBIC-JqVDWgjJT7jEGBV6HarLQmt1wa-bEpV5-UF1FC_0B0Co3F4j09Wm9ol32_pvOIP2fK07OpwDbf7zsrGgOXjXfSGiGGdiHip_XbVzrzw0lhxorNUuVmPYTXcVlewLbPqA324RhWyTr3mVi9EEhi4RSvcXFz9G39CgQAVlZ0U5qXDEDNAjws1VzAbHZI2tlEHypWom0C6F3GrkLvVckBe3TaZnHLY1n3b3bYLIcgUc47srv_ND3c-F_Lbw70OyDd-6gWw0cNaYHPqMgbVrNp_QA_xgMweW07s7j5yy1qAAAAAWIpE04A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BlackWorldMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NixaWorld")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6190680150").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
