from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "wgh_char_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "char_id" VARCHAR(64) NOT NULL UNIQUE,
    "bn_id" VARCHAR(64) NOT NULL,
    "char_name" VARCHAR(64) NOT NULL,
    "char_type" INT NOT NULL,
    "char_equip" INT NOT NULL,
    "char_race" INT NOT NULL,
    "char_camp" INT NOT NULL,
    "char_class" INT NOT NULL,
    "char_create_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "char_update_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "char_stu" INT NOT NULL,
    "char_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "wgh_group_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "group_id" VARCHAR(64) NOT NULL UNIQUE,
    "group_name" VARCHAR(64) NOT NULL,
    "group_mark" TEXT NOT NULL,
    "group_type" INT NOT NULL,
    "group_cap" VARCHAR(64) NOT NULL,
    "group_open" INT NOT NULL,
    "group_stu" INT NOT NULL,
    "group_create_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "group_update_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "group_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "wgh_member_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "member_id" VARCHAR(64) NOT NULL,
    "group_id" VARCHAR(64) NOT NULL,
    "char_id" VARCHAR(64) NOT NULL,
    "member_type" INT NOT NULL,
    "member_class" INT NOT NULL,
    "member_stu" INT NOT NULL,
    "member_create_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "member_update_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "member_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "wgh_msg_record" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "rec_id" VARCHAR(64) NOT NULL UNIQUE,
    "rec_batch" VARCHAR(64) NOT NULL,
    "msg_tmpl" VARCHAR(64) NOT NULL,
    "msg_rcv" VARCHAR(64) NOT NULL,
    "msg_data" JSONB,
    "msg_send_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "msg_stu" INT NOT NULL,
    "msg_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "wgh_user_battlenet" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "usr_uid" VARCHAR(64) NOT NULL,
    "bn_id" VARCHAR(64) NOT NULL UNIQUE,
    "usr_openid" VARCHAR(64) NOT NULL,
    "bn_tag" VARCHAR(64) NOT NULL,
    "bn_create_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "bn_update_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "bn_stu" INT,
    "bn_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "wgh_user_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "usr_id" VARCHAR(64) NOT NULL UNIQUE,
    "usr_uid" VARCHAR(64) NOT NULL UNIQUE,
    "usr_unionid" VARCHAR(64) NOT NULL,
    "usr_openid" VARCHAR(64) NOT NULL UNIQUE,
    "usr_create_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "usr_update_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "usr_stu" INT,
    "usr_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
