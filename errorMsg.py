def getMsg():
    return {
            0: "OK",
            1: "操作失败",
            2: "参数错误",
            3: "通信错误（指令发送错误）",
            4: "通信错误（指令读取错误，请重新插拔）",
            5: "通信错误（指令错误）",
            6: "密钥未设置",
            7: "操作失败，未进入发卡模式",
            8: "操作中断失败（停止发送空白卡操作时失败）",
            9: "操作中断（停止发送空白卡操作，原始操作返回）",
            10: "服务器地址未配置（1.3.0内部默认设置，不再返回）",
            11: "网络请求失败，请检查您的网络是否正常",
            12: "接口返回的数据不符合格式要求，请重新配置服务器",
            13: "hotelInfo无效",
            14: "非本酒店读卡器",
            15: "发卡器未初始化（1.3.0新增）",
            16: "设备未连接，无法操作（1.3.0新增）",
            21: "非IC卡（读取IC卡卡号时，放置卡片非IC卡）",
            26: "断开连接失败（1.3.0新增）",
            28: "配置串口失败（1.3.0新增）",
            31: "无法打开日志文件（1.3.0新增）",
            32: "发卡器不支持该指令操作，请升级硬件版本（1.4.0新增）",
            33: "发卡器不支持CPU卡操作（1.4.0新增）",
            201: "配置密钥失败",
            202: "配置卡密钥失败",
            203: "配置酒店信息失败",
            1001: "配置服务器地址失败（内部使用，暂不开放）",
            1002: "获取设备注册信息列表失败（内部使用，暂不开放）",
            1003: "找不到相关的发卡器设备（内部使用，暂不开放）",
            1004: "设备已被占用（内部使用，暂不开放）",
            1005: "设备初始化失败，需要重新插拔（内部使用，暂不开放）",
            1006: "获取设备列表失败（内部使用，暂不开放）",
            101: "其它错误",
            102: "操作超时",
            104: "IC卡存储空间不足",
            105: "解密失败或密钥未配置",
            106: "卡解密失败",
            107: "IC卡内不存在该条数据",
            108: "密文校验失败",
            109: "酒店ID未配置",
            110: "非法操作，待挂失的卡片为当前卡片",
            301: "数据解析的其他错误",
            304: "扇区空间不足",
            305: "密钥解密失败或未配置",
            307: "IC卡数据不存在",
            420: "数据未正常返回"
        }
