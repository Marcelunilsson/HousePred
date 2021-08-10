def Data_Selection(df):
    def Object_Type_Selection(df):
        Selected_Object_Types = df.loc[df['Objekttyp:S:O'].isin([
            # 'Villa',
            # 'Radhus',
            # 'Parhus',
            # 'Kedjehus',
            'Lägenhet',
            ])]
        df = Selected_Object_Types
        return df

    def Municipality_Selection(df):
        Selected_Municipalities = df[df['Kommun:S:K'].isin([
<<<<<<< HEAD
            #'stockholm',
            #'Göteborg',
=======
            'stockholm',
            'Göteborg',
>>>>>>> 2fee0243e3147665a6c579b7cb1b59ff7bebd945
            'Malmö',
            #'Ale',
            #'Alingsås',
            #'Boden',
            #'Botkyrka',
            #'Danderyd',
            #'Ekerö',
            #'Enköping',
            #'Eslöv',
            #'Falkenberg',
            #'Falköping',
            #'Gislaved',
            #'Gotland',
            #'Haninge',
            #'Huddinge',
            #'Hudiksvall',
            #'Härryda',
            #'Hässleholm',
            #'Järfälla',
            #'Karlshamn',
            #'Karlskoga',
            #'Katrineholm',
            #'Kungsbacka',
            #'Kävlinge',
            #'Ljungby',
            #'Mark',
            #'Mjölby',
            #'Mölndal',
            #'Nacka',
            #'Norrtälje',
            #'Nynäshamn',
            #'Nässjö',
            #'Partille',
            #'Piteå',
            #'Ronneby',
            #'Sigtuna',
            #'Solna',
            #'Strängnäs',
            #'Sundbyberg',
            #'Tyresö',
            #'Täby',
            #'Upplands-Bro',
            #'Vellinge',
            #'Vänersborg',
            #'Värmdö',
            #'Värnamo',
            #'Västervik',
            #'Ystad',
            #'Österåker',
            #'Uppsala',
            #'Borås',
            #'Eskilstuna',
            #'Gävle',
            #'Halmstad',
            #'Helsingborg',
            #'Jönköping',
            #'Linköping',
            #'Lund',
            #'Norrköping',
            #'Örebro',
            #'Södertälje',
            #'Sollentuna',
            #'Umeå',
            #'Västerås',
            #'Växjö',
            #'skellefteå',
            #'alingsås',
            #'Borlänge',
            #'falun',
            #'kalmar',
            #'karlskoga',
            #'karlskrona',
            #'Karlstad',
            #'Kristianstad',
            #'kungälv',
            #'landskrona',
            #'lerum',
            #'Lidingö',
            #'Luleå',
            #'motala',
            #'nyköping',
            #'Östersund',
            #'sandviken',
            #'skövde',
            #'Sundsvall',
            #'trelleborg',
            #'Trollhättan',
            #'uddevalla',
            #'vallentuna',
            #'varberg',
            #'ängelholm',
            #'Örnsköldsvik'
        ])]
        df = Selected_Municipalities
        return df

    df = Object_Type_Selection(df)
    df = Municipality_Selection(df)
    return df

def Defining_X_and_Y(df):

    Selected_X_Features = df[[

        # Standard
            # 'Objekttyp:S:O', #S1
            # 'Gata:S:G', #S3
<<<<<<< HEAD
            # 'Stadsdel:S:Sd',  # S5
            # 'Stad:S:S', #S6
            # 'Kommun:S:K', #S7
            # 'Landskap:S:Ls', #S8
             'Rum:A(st):O',  # S9
             'Kvm:A(st):O',  # S10

             'Månad:N:M', #S13
             'År:N:Å',  # S14
             'Lat:N:O',  # S15
             'Long:N:O',  # S16
            # 'KvmTomt:A(st):O', #S18
            # 'HarTomt:B:O', #S19
            #'Lat5Deci:N:O',  # S20
            #'Long5Deci:N:O',  # S21
            #'Lat4Deci:N:O',  # S22
            #'Long4Deci:N:O',  # S23
            #'Lat3Deci:N:O',  # S24
            # 'Long3Deci:N:O',  # S25
            # 'Lat2Deci:N:O',  # S26
            # 'Long2Deci:N:O',  # S27
            # 'Lat1Deci:N:O',  # S28
            # 'Long1Deci:N:O',  # S29
            # 'Lat0Deci:N:O',  # S30
            # 'Long0Deci:N:O',  # S31
            # 'KvmPris:A(kr):O', #S32

        # Ekonomi
            # 'KPI:N:LÅ',  # E1
            # 'GDP:A(Giga$):LÅ',  # E2
            # 'Arbetslöshet:P:L',  # E3
            # 'RepoRänta:P:LD',  # E4
            # 'OMXIndex:N:LD',  # E5
            # 'SkattTotal:P:KÅ',  # E6
            # 'SkattRegering:P:KÅ',  # E7
            # 'SkattKommun:P:KÅ',  # E8
            # 'Snittslön:A(kr/m):LÅ',  # E9
            # 'SnittslönMän:A(tkr/å):KÅ',  # E10
            # 'SnittslönKvinnor:A(tkr/å):KÅ',  # E11
            # 'Snittslön:A(tkr/å):KÅ',  # E12
            # 'PenningMängdM1:A(mkr):LM',  # E13
            # 'PenningMängdM2:A(mkr):LM',  # E14
=======
            'Stadsdel:S:Sd',  # S5
            'Stad:S:S', #S6
            'Kommun:S:K', #S7
            'Landskap:S:Ls', #S8
            'Rum:A(st):O',  # S9
            'Kvm:A(st):O',  # S10

            # 'Månad:N:M', #S13
            'År:N:Å',  # S14
            'Lat:N:O',  # S15
            'Long:N:O',  # S16
            # 'KvmTomt:A(st):O', #S18
            # 'HarTomt:B:O', #S19
            'Lat5Deci:N:O',  # S20
            'Long5Deci:N:O',  # S21
            'Lat4Deci:N:O',  # S22
            'Long4Deci:N:O',  # S23
            'Lat3Deci:N:O',  # S24
            'Long3Deci:N:O',  # S25
            'Lat2Deci:N:O',  # S26
            'Long2Deci:N:O',  # S27
            'Lat1Deci:N:O',  # S28
            'Long1Deci:N:O',  # S29
            'Lat0Deci:N:O',  # S30
            'Long0Deci:N:O',  # S31
            # 'KvmPris:A(kr):O', #S32

        # Ekonomi
            'KPI:N:LÅ',  # E1
            'GDP:A(Giga$):LÅ',  # E2
            'Arbetslöshet:P:L',  # E3
            'RepoRänta:P:LD',  # E4
            'OMXIndex:N:LD',  # E5
            'SkattTotal:P:KÅ',  # E6
            'SkattRegering:P:KÅ',  # E7
            'SkattKommun:P:KÅ',  # E8
            'Snittslön:A(kr/m):LÅ',  # E9
            'SnittslönMän:A(tkr/å):KÅ',  # E10
            'SnittslönKvinnor:A(tkr/å):KÅ',  # E11
            'Snittslön:A(tkr/å):KÅ',  # E12
            'PenningMängdM1:A(mkr):LM',  # E13
            'PenningMängdM2:A(mkr):LM',  # E14
>>>>>>> 2fee0243e3147665a6c579b7cb1b59ff7bebd945

        # Utbildning
            # 'UtbFörGym<9År:A(st):KÅ', #U1
            # 'UtbFörGym9År:A(st):KÅ', #U2
            # 'UtbGym<=2År', #U3
            # 'UtbGym3År:A(st):KÅ', #U4
            # 'UtbEfterGym<3År:A(st):KÅ', #U5
            # 'UtbEfterGym>=3År:A(st):KÅ', #U6
            # 'UtbForskare:A(st):KÅ', #U7
            # 'UtbUppgSaknas:A(st):KÅ', #U8
<<<<<<< HEAD
            # 'UtbFörGym<9År:A(st):KÅ_procent',  # U9
            # 'UtbFörGym9År:A(st):KÅ_procent',  # U10
            # 'UtbGym<=2År_procent',  # U11
            # 'UtbGym3År:A(st):KÅ_procent',  # U12
            # 'UtbEfterGym<3År:A(st):KÅ_procent',  # U13
            # 'UtbEfterGym>=3År:A(st):KÅ_procent',  # U14
            # 'UtbForskare:A(st):KÅ_procent',  # U15
            # 'UtbUppgSaknas:A(st):KÅ_procent',  # U16
=======
            'UtbFörGym<9År:A(st):KÅ_procent',  # U9
            'UtbFörGym9År:A(st):KÅ_procent',  # U10
            'UtbGym<=2År_procent',  # U11
            'UtbGym3År:A(st):KÅ_procent',  # U12
            'UtbEfterGym<3År:A(st):KÅ_procent',  # U13
            'UtbEfterGym>=3År:A(st):KÅ_procent',  # U14
            'UtbForskare:A(st):KÅ_procent',  # U15
            'UtbUppgSaknas:A(st):KÅ_procent',  # U16
>>>>>>> 2fee0243e3147665a6c579b7cb1b59ff7bebd945

        # Rörelser
            # 'Inflyttning:A(st):KÅ', #R1
            # 'Utflyttning:A(st):KÅ', #R2
            # 'Invandring:A(st):KÅ', #R3
            # 'Utvandring:A(st):KÅ', #R4
            # 'FlyttningÖverskott:A(st):KÅ', #R5
            # 'InvandringÖverskott:A(st):KÅ', #R6
<<<<<<< HEAD
            # 'Inflyttning:A(st):KÅ_procent',  # R7
            # 'Utflyttning:A(st):KÅ_procent',  # R8
            # 'Invandring:A(st):KÅ_procent',  # R9
            # 'Utvandring:A(st):KÅ_procent',  # R10
            # 'FlyttningÖverskott:A(st):KÅ_procent',  # R11
            # 'InvandringÖverskott:A(st):KÅ_procent',  # R12
=======
            'Inflyttning:A(st):KÅ_procent',  # R7
            'Utflyttning:A(st):KÅ_procent',  # R8
            'Invandring:A(st):KÅ_procent',  # R9
            'Utvandring:A(st):KÅ_procent',  # R10
            'FlyttningÖverskott:A(st):KÅ_procent',  # R11
            'InvandringÖverskott:A(st):KÅ_procent',  # R12
>>>>>>> 2fee0243e3147665a6c579b7cb1b59ff7bebd945

        # Origin
            # 'FöddaISverige:A(st):KÅ', #O1
            # 'FöddaIUtland:A(st):KÅ', #O2
<<<<<<< HEAD
            # 'FöddaISverige:A(st):KÅ_procent',  # O3
            # 'FöddaIUtland:A(st):KÅ_procent',  # O4

            # Demografi
            # 'AntalMän:A(st):KÅ',  # D1
            # 'AntalKvinnor:A(st):KÅ',  # D2
            # 'AntalMän:A(st):KÅ_procent',  # D3
            # 'AntalKvinnor:A(st):KÅ_procent',  # D4
            # 'AntalInvånare:A(st):KÅ',  # D5
            # 'InvånareKm:A(st):KÅ',  # D6
            # 'MedelålderMän:A(st):KÅ',  # D7
            # 'MedelålderKvinnor:A(st):KÅ',  # D8
            # 'Medelålder:A(st):KÅ',  # D9
            # 'InvånareKm:A(st):KÅ_procent',  # D10
=======
            'FöddaISverige:A(st):KÅ_procent',  # O3
            'FöddaIUtland:A(st):KÅ_procent',  # O4

            # Demografi
            'AntalMän:A(st):KÅ',  # D1
            'AntalKvinnor:A(st):KÅ',  # D2
            'AntalMän:A(st):KÅ_procent',  # D3
            'AntalKvinnor:A(st):KÅ_procent',  # D4
            'AntalInvånare:A(st):KÅ',  # D5
            'InvånareKm:A(st):KÅ',  # D6
            'MedelålderMän:A(st):KÅ',  # D7
            'MedelålderKvinnor:A(st):KÅ',  # D8
            'Medelålder:A(st):KÅ',  # D9
            'InvånareKm:A(st):KÅ_procent',  # D10
>>>>>>> 2fee0243e3147665a6c579b7cb1b59ff7bebd945

        # Kriminalitet
            # 'KrimMisshandel:A(st):KÅ', #K1
            # 'KrimNarkotika:A(st):KÅ', #K2
            # 'KrimNarkotikaÖverlåtelse:A(st):KÅ', #K3
<<<<<<< HEAD
            # 'KrimMisshandel:A(st):KÅ_procent',  # K4
            # 'KrimNarkotika:A(st):KÅ_procent',  # K5
            # 'KrimNarkotikaÖverlåtelse:A(st):KÅ_procent',  # K6
=======
            'KrimMisshandel:A(st):KÅ_procent',  # K4
            'KrimNarkotika:A(st):KÅ_procent',  # K5
            'KrimNarkotikaÖverlåtelse:A(st):KÅ_procent',  # K6
>>>>>>> 2fee0243e3147665a6c579b7cb1b59ff7bebd945

        # Mean-features
            #'MedelKvmPrisRum:A(kr):Sd',  # M1
            #'MedelKvmPrisRum:A(kr):S',  # M2
            #'MedelKvmPrisRum:A(kr):K',  # M3
            #'MedelPrisRum:A(kr):Sd',  # M4
            #'MedelPrisRum:A(kr):S',  # M5
            #'MedelPrisRum:A(kr):K',  # M6
            #'MedelKvmPrisRum:A(kr):SdÅ',  # M7
            #'MedelKvmPrisRum:A(kr):SÅ',  # M8
            #'MedelKvmPrisRum:A(kr):KÅ',  # M9
            #'MedelPrisRum:A(kr):SdÅ',  # M10
            #'MedelPrisRum:A(kr):SÅ',  # M11
            #'MedelPrisRum:A(kr):KÅ',  # M12
            #'MedelKvmPrisRumLatLong0Deci:A(kr):',  # M13
            #'MedelKvmPrisRumLatLong1Deci:A(kr):',  # M14
            #'MedelKvmPrisRumLatLong2Deci:A(kr):',  # M15
            #'MedelKvmPrisRumLatLong3Deci:A(kr):',  # M16
            #'MedelKvmPrisRumLatLong0Deci:A(kr):Å',  # M17
            #'MedelKvmPrisRumLatLong1Deci:A(kr):Å',  # M18
            #'MedelKvmPrisRumLatLong2Deci:A(kr):Å',  # M19
            #'MedelKvmPrisRumLatLong3Deci:A(kr):Å',  # M20
        ]]

    X = Selected_X_Features
    y = df['Pris:A(kr):O']

    print(f"X.shape: {X.shape} \ny.shape: {y.shape} \nNo diff between X.shape and y.shape: {y.shape[0] == X.shape[0]}")
    return X, y
