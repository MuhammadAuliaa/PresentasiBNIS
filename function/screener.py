import yfinance as yf

def fetch_stocks(stock_universe):
        # Manual lists of stock tickers for each universe
        stock_universe_mapping = {
            "IHSG": ["AALI","ABBA","ABDA","ABMM","ACES","ACRO","ACST","ADCP","ADES","ADHI","ADMF","ADMG","ADMR","ADRO","AEGS","AGAR","AGII","AGRO","AGRS","AHAP","AIMS","AISA","AKKU","AKPI","AKRA","AKSI","ALDO","ALII","ALKA","ALMI","ALTO","AMAG","AMAN","AMAR","AMFG","AMIN","AMMN","AMMS","AMOR","AMRT","ANDI","ANJT","ANTM","APEX","APIC","APII","APLI","APLN","ARCI","AREA","ARGO","ARII","ARKA","ARKO","ARMY","ARNA","ARTA","ARTI","ARTO","ASBI","ASDM","ASGR","ASHA","ASII","ASJT","ASLC","ASLI","ASMI","ASPI","ASRI","ASRM","ASSA","ATAP","ATIC","ATLA","AUTO","AVIA","AWAN","AXIO","AYAM","AYLS","BABP","BABY","BACA","BAIK","BAJA","BALI","BANK","BAPA","BAPI","BATA","BATR","BAUT","BAYU","BBCA","BBHI","BBKP","BBLD","BBMD","BBNI","BBRI","BBRM","BBSI","BBSS","BBTN","BBYB","BCAP","BCIC","BCIP","BDKR","BDMN","BEBS","BEEF","BEER","BEKS","BELI","BELL","BESS","BEST","BFIN","BGTG","BHAT","BHIT","BIKA","BIKE","BIMA","BINA","BINO","BIPI","BIPP","BIRD","BISI","BJBR","BJTM","BKDP","BKSL","BKSW","BLTA","BLTZ","BLUE","BMAS","BMBL","BMHS","BMRI","BMSR","BMTR","BNBA","BNBR","BNGA","BNII","BNLI","BOBA","BOGA","BOLA","BOLT","BOSS","BPFI","BPII","BPTR","BRAM","BREN","BRIS","BRMS","BRNA","BRPT","BSBK","BSDE","BSIM","BSML","BSSR","BSWD","BTEK","BTEL","BTON","BTPN","BTPS","BUAH","BUDI","BUKA","BUKK","BULL","BUMI","BUVA","BVIC","BWPT","BYAN","CAKK","CAMP","CANI","CARE","CARS","CASA","CASH","CASS","CBMF","CBPE","CBRE","CBUT","CCSI","CEKA","CENT","CFIN","CGAS","CHEM","CHIP","CINT","CITA","CITY","CLAY","CLEO","CLPI","CMNP","CMNT","CMPP","CMRY","CNKO","CNMA","CNTX","COAL","COCO","COWL","CPIN","CPRI","CPRO","CRAB","CRSN","CSAP","CSIS","CSMI","CSRA","CTBN","CTRA","CTTH","CUAN","CYBR","DADA","DART","DATA","DAYA","DCII","DEAL","DEFI","DEPO","DEWA","DEWI","DFAM","DGIK","DGNS","DIGI","DILD","DIVA","DKFT","DLTA","DMAS","DMMX","DMND","DNAR","DNET","DOID","DOOH","DPNS","DPUM","DRMA","DSFI","DSNG","DSSA","DUCK","DUTI","DVLA","DWGL","DYAN","EAST","ECII","EDGE","EKAD","ELIT","ELPI","ELSA","ELTY","EMDE","EMTK","ENAK","ENRG","ENVY","ENZO","EPAC","EPMT","ERAA","ERAL","ERTX","ESIP","ESSA","ESTA","ESTI","ETWA","EURO","EXCL","FAPA","FAST","FASW","FILM","FIMP","FIRE","FISH","FITT","FLMC","FMII","FOLK","FOOD","FORU","FORZ","FPNI","FREN","FUJI","FUTR","FWCT","GAMA","GDST","GDYR","GEMA","GEMS","GGRM","GGRP","GHON","GIAA","GJTL","GLOB","GLVA","GMFI","GMTD","GOLD","GOLL","GOOD","GOTO","GPRA","GPSO","GRIA","GRPH","GRPM","GSMF","GTBO","GTRA","GTSI","GULA","GWSA","GZCO","HADE","HAIS","HAJJ","HALO","HATM","HBAT","HDFA","HDIT","HDTX","HEAL","HELI","HERO","HEXA","HILL","HITS","HKMU","HMSP","HOKI","HOME","HOMI","HOPE","HOTL","HRME","HRTA","HRUM","HUMI","HYGN","IATA","IBFN","IBOS","IBST","ICBP","ICON","IDEA","IDPR","IFII","IFSH","IGAR","IIKP","IKAI","IKAN","IKBI","IKPM","IMAS","IMJS","IMPC","INAF","INAI","INCF","INCI","INCO","INDF","INDO","INDR","INDS","INDX","INDY","INET","INKP","INOV","INPC","INPP","INPS","INRU","INTA","INTD","INTP","IOTF","IPAC","IPCC","IPCM","IPOL","IPPE","IPTV","IRRA","IRSX","ISAP","ISAT","ISSP","ITIC","ITMA","ITMG","JARR","JAST","JATI","JAWA","JAYA","JECC","JGLE","JIHD","JKON","JKSW","JMAS","JPFA","JRPT","JSKY","JSMR","JSPT","JTPE","KAEF","KARW","KAYU","KBAG","KBLI","KBLM","KBLV","KBRI","KDSI","KDTN","KEEN","KEJU","KETR","KIAS","KICI","KIJA","KING","KINO","KIOS","KJEN","KKES","KKGI","KLAS","KLBF","KLIN","KMDS","KMTR","KOBX","KOCI","KOIN","KOKA","KONI","KOPI","KOTA","KPAL","KPAS","KPIG","KRAH","KRAS","KREN","KRYA","KUAS","LABA","LAJU","LAND","LAPD","LCGP","LCKM","LEAD","LFLO","LIFE","LINK","LION","LIVE","LMAS","LMAX","LMPI","LMSH","LOPI","LPCK","LPGI","LPIN","LPKR","LPLI","LPPF","LPPS","LRNA","LSIP","LTLS","LUCK","LUCY","MABA","MAGP","MAHA","MAIN","MAMI","MANG","MAPA","MAPB","MAPI","MARI","MARK","MASA","MASB","MAXI","MAYA","MBAP","MBMA","MBSS","MBTO","MCAS","MCOL","MCOR","MDIA","MDKA","MDKI","MDLN","MDRN","MEDC","MEDS","MEGA","MEJA","MENN","MERK","META","MFIN","MFMI","MGLV","MGNA","MGRO","MHKI","MICE","MIDI","MIKA","MINA","MIRA","MITI","MKAP","MKNT","MKPI","MKTR","MLBI","MLIA","MLPL","MLPT","MMIX","MMLP","MNCN","MOLI","MORA","MPIX","MPMX","MPOW","MPPA","MPRO","MPXL","MRAT","MREI","MSIE","MSIN","MSJA","MSKY","MSTI","MTDL","MTEL","MTFN","MTLA","MTMH","MTPS","MTRA","MTSM","MTWI","MUTU","MYOH","MYOR","MYRX","MYTX","NANO","NASA","NASI","NATO","NAYZ","NCKL","NELY","NETV","NFCX","NICE","NICK","NICL","NIKL","NINE","NIPS","NIRO","NISP","NOBU","NPGF","NRCA","NSSS","NTBK","NUSA","NZIA","OASA","OBMD","OCAP","OILS","OKAS","OLIV","OMED","OMRE","OPMS","PACK","PADA","PADI","PALM","PAMG","PANI","PANR","PANS","PBID","PBRX","PBSA","PCAR","PDES","PDPP","PEGE","PEHA","PEVE","PGAS","PGEO","PGJO","PGLI","PGUN","PICO","PIPA","PJAA","PKPK","PLAN","PLAS","PLIN","PMJS","PMMP","PNBN","PNBS","PNGO","PNIN","PNLF","PNSE","POLA","POLI","POLL","POLU","POLY","POOL","PORT","POSA","POWR","PPGL","PPRE","PPRI","PPRO","PRAS","PRAY","PRDA","PRIM","PSAB","PSDN","PSGO","PSKT","PSSI","PTBA","PTDU","PTIS","PTMP","PTPP","PTPS","PTPW","PTRO","PTSN","PTSP","PUDP","PURA","PURE","PURI","PWON","PYFA","PZZA","RAAM","RAFI","RAJA","RALS","RANC","RBMS","RCCC","RDTX","REAL","RELF","RELI","RGAS","RICY","RIGS","RIMO","RISE","RMKE","RMKO","ROCK","RODA","RONY","ROTI","RSCH","RSGK","RUIS","RUNS","SAFE","SAGE","SAME","SAMF","SAPX","SATU","SBAT","SBMA","SCCO","SCMA","SCNP","SCPI","SDMU","SDPC","SDRA","SEMA","SFAN","SGER","SGRO","SHID","SHIP","SICO","SIDO","SILO","SIMA","SIMP","SINI","SIPD","SKBM","SKLT","SKRN","SKYB","SLIS","SMAR","SMBR","SMCB","SMDM","SMDR","SMGA","SMGR","SMIL","SMKL","SMKM","SMLE","SMMA","SMMT","SMRA","SMRU","SMSM","SNLK","SOCI","SOFA","SOHO","SOLA","SONA","SOSS","SOTS","SOUL","SPMA","SPTO","SQMI","SRAJ","SRIL","SRSN","SRTG","SSIA","SSMS","SSTM","STAA","STAR","STRK","STTP","SUGI","SULI","SUNI","SUPR","SURE","SURI","SWAT","SWID","TALF","TAMA","TAMU","TAPG","TARA","TAXI","TAYS","TBIG","TBLA","TBMS","TCID","TCPI","TDPM","TEBE","TECH","TELE","TFAS","TFCO","TGKA","TGRA","TGUK","TIFA","TINS","TIRA","TIRT","TKIM","TLDN","TLKM","TMAS","TMPO","TNCA","TOBA","TOOL","TOPS","TOSK","TOTL","TOTO","TOWR","TOYS","TPIA","TPMA","TRAM","TRGU","TRIL","TRIM","TRIN","TRIO","TRIS","TRJA","TRON","TRST","TRUE","TRUK","TRUS","TSPC","TUGU","TYRE","UANG","UCID","UDNG","UFOE","ULTJ","UNIC","UNIQ","UNIT","UNSP","UNTD","UNTR","UNVR","URBN","UVCR","VAST","VICI","VICO","VINS","VISI","VIVA","VKTR","VOKS","VRNA","VTNY","WAPO","WEGE","WEHA","WGSH","WICO","WIDI","WIFI","WIIM","WIKA","WINE","WINR","WINS","WIRG","WMPP","WMUU","WOMF","WOOD","WOWS","WSBP","WSKT","WTON","YELO","YPAS","YULE","ZATA","ZBRA","ZINC","ZONE","ZYRX"],
            "LQ45": ["ACES", "ADRO", "AKRA", "AMRT", "ANTM", "ARTO", "ASII", "BBCA", "BBNI", "BBRI", "BBTN", "BMRI", "BRIS", "BRPT", "BUKA", "CPIN", "EMTK", "ESSA", "EXCL", "GGRM", "GOTO", "HRUM", "ICBP", "INCO", "INDF", "INKP", "INTP", "ITMG", "KLBF", "MAPI", "MBMA", "MDKA", "MEDC", "MTEL", "PGAS", "PGEO", "PTBA", "PTMP", "SIDO", "SMGR", "SRTG", "TLKM", "TOWR", "UNTR", "UNVR"],
            "Syariah": ["TLKM", "BRIS"]  # Example tickers for Syariah
        }
        tickers = [ticker + ".JK" for ticker in stock_universe_mapping.get(stock_universe, [])]
        stocks = {ticker: yf.Ticker(ticker).info for ticker in tickers}
        return stocks

def apply_filter(stocks, feature, operator, value1, value2=None):
    def get_numeric_value(value):
        if isinstance(value, str) and value.endswith('%'):
            return float(value.rstrip('%'))
        return value

    value1 = get_numeric_value(value1)
    if value2 is not None:
        value2 = get_numeric_value(value2)

    if operator == '>':
        filtered_stocks = {ticker: info for ticker, info in stocks.items() if get_numeric_value(info.get(feature, 0)) > value1}
    elif operator == '<':
        filtered_stocks = {ticker: info for ticker, info in stocks.items() if get_numeric_value(info.get(feature, 0)) < value1}
    elif operator == '>=':
        filtered_stocks = {ticker: info for ticker, info in stocks.items() if get_numeric_value(info.get(feature, 0)) >= value1}
    elif operator == '<=':
        filtered_stocks = {ticker: info for ticker, info in stocks.items() if get_numeric_value(info.get(feature, 0)) <= value1}
    elif operator == '=':
        filtered_stocks = {ticker: info for ticker, info in stocks.items() if get_numeric_value(info.get(feature, 0)) == value1}
    elif operator == 'between':
        filtered_stocks = {ticker: info for ticker, info in stocks.items() if value1 <= get_numeric_value(info.get(feature, 0)) <= value2}
    else:
        filtered_stocks = stocks
    return filtered_stocks

def calculate_high_to_close(info):
    high = info.get('dayHigh', 0)
    low = info.get('dayLow', 0)
    if high != 0:
        return ((high - low) / high) * 100
    else:
        return None  # Return None if high is zero to handle edge case

def calculate_1_day_price_returns(info):
    open_price = info.get('open', 0)
    close_price = info.get('regularMarketPreviousClose', 0)
    if open_price != 0:
        return ((close_price - open_price) / open_price) * 100
    else:
        return None  # Return None if open price is zero to handle edge case