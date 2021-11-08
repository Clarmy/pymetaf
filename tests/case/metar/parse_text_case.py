PARSE_TEXT_CASE = [{
    'kwargs': {
        'text': 'METAR ZBAA 311400Z 01002MPS CAVOK 14/12 Q1009 NOSIG=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZBAA',
        'auto': False,
        'datetime': '2021-05-31T14:00:00+00:00',
        'wind_direction': 10,
        'wind_direction_units': 'degree',
        'wind_speed': 2,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': None,
        'visibility': 99999,
        'visibility_units': 'm',
        'cavok': True,
        'temperature': 14,
        'dew_temperature': 12,
        'temperature_units': 'degree C',
        'qnh': 1009,
        'qnh_units': 'hPa',
        'cloud': None,
        'weather': None
    }
}, {
    'kwargs': {
        'text':
        'METAR ZBAA 310630Z 09002MPS 050V140 8000 -SHRA NSC 19/14 Q1007 NOSIG=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZBAA',
        'auto': False,
        'datetime': '2021-05-31T06:30:00+00:00',
        'wind_direction': 90,
        'wind_direction_units': 'degree',
        'wind_speed': 2,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': (50, 140),
        'visibility': 8000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 19,
        'dew_temperature': 14,
        'temperature_units': 'degree C',
        'qnh': 1007,
        'qnh_units': 'hPa',
        'cloud': [{'cloud_height': None, 'cloud_height_units': 'm', 'cloud_mask': 'NSC', 'cloud_type': None}],
        'weather': ['-SHRA']
    }
}, {
    'kwargs': {
        'text': 'METAR ZBAA 310530Z VRB02MPS 8000 NSC 19/13 Q1007 NOSIG=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZBAA',
        'auto': False,
        'datetime': '2021-05-31T05:30:00+00:00',
        'wind_direction': None,
        'wind_direction_units': 'degree',
        'wind_speed': 2,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': None,
        'visibility': 8000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 19,
        'dew_temperature': 13,
        'temperature_units': 'degree C',
        'qnh': 1007,
        'qnh_units': 'hPa',
        'cloud': [{'cloud_height': None, 'cloud_height_units': 'm', 'cloud_mask': 'NSC', 'cloud_type': None}],
        'weather': None
    }
}, {
    'kwargs': {
        'text':
        'METAR ZBAA 310230Z 03002MPS 330V080 6000 -SHRA NSC 16/14 Q1008 NOSIG=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZBAA',
        'auto': False,
        'datetime': '2021-05-31T02:30:00+00:00',
        'wind_direction': 30,
        'wind_direction_units': 'degree',
        'wind_speed': 2,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': (330, 80),
        'visibility': 6000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 16,
        'dew_temperature': 14,
        'temperature_units': 'degree C',
        'qnh': 1008,
        'qnh_units': 'hPa',
        'cloud': [{'cloud_height': None, 'cloud_height_units': 'm', 'cloud_mask': 'NSC', 'cloud_type': None}],
        'weather': ['-SHRA']
    }
}, {
    'kwargs': {
        'text':
        'METAR ZBHD 311500Z VRB03MPS 3000 TS BR FEW040CB 22/19 Q1006 NOSIG=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZBHD',
        'auto': False,
        'datetime': '2021-05-31T15:00:00+00:00',
        'wind_direction': None,
        'wind_direction_units': 'degree',
        'wind_speed': 3,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': None,
        'visibility': 3000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 22,
        'dew_temperature': 19,
        'temperature_units': 'degree C',
        'qnh': 1006,
        'qnh_units': 'hPa',
        'cloud': [{'cloud_height': 800, 'cloud_height_units': 'm', 'cloud_mask': 'FEW', 'cloud_type': 'cumulonimbus'}],
        'weather': ['TS', 'BR']
    }
}, {
    'kwargs': {
        'text':
        'SPECI ZBHD 311029Z 30009MPS 7000 -TSRA SCT030CB BKN046 25/17 Q1007 NOSIG=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'SPECI',
        'icao': 'ZBHD',
        'auto': False,
        'datetime': '2021-05-31T10:29:00+00:00',
        'wind_direction': 300,
        'wind_direction_units': 'degree',
        'wind_speed': 9,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': None,
        'visibility': 7000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 25,
        'dew_temperature': 17,
        'temperature_units': 'degree C',
        'qnh': 1007,
        'qnh_units': 'hPa',
        'cloud': [
            {'cloud_height': 920, 'cloud_height_units': 'm',
                'cloud_mask': 'BKN', 'cloud_type': None},
            {'cloud_height': 600, 'cloud_height_units': 'm',
                'cloud_mask': 'SCT', 'cloud_type': 'cumulonimbus'}
        ],
        'weather': ['-TSRA']
    }
}, {
    'kwargs': {
        'text':
        'SPECI ZBHD 311029Z 30009MPS 7000 -TSRA SCT030CB BKN046 25/17 Q1007 NOSIG',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'SPECI',
        'icao': 'ZBHD',
        'auto': False,
        'datetime': '2021-05-31T10:29:00+00:00',
        'wind_direction': 300,
        'wind_direction_units': 'degree',
        'wind_speed': 9,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': None,
        'visibility': 7000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 25,
        'dew_temperature': 17,
        'temperature_units': 'degree C',
        'qnh': 1007,
        'qnh_units': 'hPa',
        'cloud': [
            {'cloud_height': 920, 'cloud_height_units': 'm',
                'cloud_mask': 'BKN', 'cloud_type': None},
            {'cloud_height': 600, 'cloud_height_units': 'm',
                'cloud_mask': 'SCT', 'cloud_type': 'cumulonimbus'},
        ],
        'weather': ['-TSRA']
    }
}, {
    'kwargs': {
        'text':
        'METAR ZBCZ 161200Z AUTO 22004MPS 8000 // ////// 21/19 Q1008=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZBCZ',
        'auto': True,
        'datetime': '2021-05-16T12:00:00+00:00',
        'wind_direction': 220,
        'wind_direction_units': 'degree',
        'wind_speed': 4,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': None,
        'visibility': 8000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 21,
        'dew_temperature': 19,
        'temperature_units': 'degree C',
        'qnh': 1008,
        'qnh_units': 'hPa',
        'cloud': None,
        'weather': None
    }
}, {
    'kwargs': {
        'text':
        'METAR ZBCZ 161200Z AUTO 22004MPS 8000 // ////// 21/19 Q1008',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZBCZ',
        'auto': True,
        'datetime': '2021-05-16T12:00:00+00:00',
        'wind_direction': 220,
        'wind_direction_units': 'degree',
        'wind_speed': 4,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': None,
        'visibility': 8000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 21,
        'dew_temperature': 19,
        'temperature_units': 'degree C',
        'qnh': 1008,
        'qnh_units': 'hPa',
        'cloud': None,
        'weather': None
    }
}, {
    'kwargs': {
        'text':
        'SPECI ZUUU 160837Z 02004MPS 340V040 3500 SHRA BR FEW006 FEW026CB SCT026 25/25 Q1001 BECMG TL0930 -SHRA=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'SPECI',
        'icao': 'ZUUU',
        'auto': False,
        'datetime': '2021-05-16T08:37:00+00:00',
        'wind_direction': 20,
        'wind_direction_units': 'degree',
        'wind_speed': 4,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': (340, 40),
        'visibility': 3500,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 25,
        'dew_temperature': 25,
        'temperature_units': 'degree C',
        'qnh': 1001,
        'qnh_units': 'hPa',
        'cloud': [
            {'cloud_height': 120, 'cloud_height_units': 'm',
             'cloud_mask': 'FEW', 'cloud_type': None},
            {'cloud_height': 520, 'cloud_height_units': 'm',
                'cloud_mask': 'FEW', 'cloud_type': 'cumulonimbus'},
            {'cloud_height': 520, 'cloud_height_units': 'm',
                'cloud_mask': 'SCT', 'cloud_type': None}
        ],
        'weather': ['SHRA', 'BR']
    }
}, {
    'kwargs': {
        'text':
        'METAR ZUUU 161030Z 02005MPS 330V050 8000 FEW006 FEW026TCU SCT026 24/22 Q1002 NOSIG=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZUUU',
        'auto': False,
        'datetime': '2021-05-16T10:30:00+00:00',
        'wind_direction': 20,
        'wind_direction_units': 'degree',
        'wind_speed': 5,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': (330, 50),
        'visibility': 8000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 24,
        'dew_temperature': 22,
        'temperature_units': 'degree C',
        'qnh': 1002,
        'qnh_units': 'hPa',
        'cloud': [
            {'cloud_height': 120, 'cloud_height_units': 'm',
             'cloud_mask': 'FEW', 'cloud_type': None},
            {'cloud_height': 520, 'cloud_height_units': 'm',
                'cloud_mask': 'FEW', 'cloud_type': 'altocumulus'},
            {'cloud_height': 520, 'cloud_height_units': 'm',
                'cloud_mask': 'SCT', 'cloud_type': None}
        ],
        'weather': None
    }
}, {
    'kwargs': {
        'text':
        'METAR RCKH 160600Z VRB03KT 2500 SHRA BR SCT003 BKN006 OVC020 26/26 Q1008 TEMPO 5000 -SHRA RMK A2977 RA AMT 5.4MM=',
        'year': 2021,
        'month': 5
    },
    'result': {
        'kind': 'METAR',
        'icao': 'RCKH',
        'auto': False,
        'datetime': '2021-05-16T06:00:00+00:00',
        'wind_direction': None,
        'wind_direction_units': 'degree',
        'wind_speed': 1,
        'wind_speed_units': 'm/s',
        'gust': None,
        'wind_direction_range': None,
        'visibility': 2500,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 26,
        'dew_temperature': 26,
        'temperature_units': 'degree C',
        'qnh': 1008,
        'qnh_units': 'hPa',
        'cloud': [
            {'cloud_height': 120, 'cloud_height_units': 'm',
             'cloud_mask': 'BKN', 'cloud_type': None},
            {'cloud_height': 400, 'cloud_height_units': 'm',
                'cloud_mask': 'OVC', 'cloud_type': None},
            {'cloud_height': 60, 'cloud_height_units': 'm',
                'cloud_mask': 'SCT', 'cloud_type': None}
        ],
        'weather': ['SHRA', 'BR']
    }
}, {
    'kwargs': {
        'text':
        'METAR ZYAS 250500Z 21009G14MPS 6000 NSC 18/08 Q1018 NOSIG',
        'year': 2021,
        'month': 10
    },
    'result': {
        'kind': 'METAR',
        'icao': 'ZYAS',
        'auto': False,
        'datetime': '2021-10-25T05:00:00+00:00',
        'wind_direction': 210,
        'wind_direction_units': 'degree',
        'wind_speed': 9,
        'wind_speed_units': 'm/s',
        'gust': 14,
        'wind_direction_range': None,
        'visibility': 6000,
        'visibility_units': 'm',
        'cavok': False,
        'temperature': 18,
        'dew_temperature': 8,
        'temperature_units': 'degree C',
        'qnh': 1018,
        'qnh_units': 'hPa',
        'cloud': [
            {'cloud_height': None, 'cloud_height_units': 'm',
             'cloud_mask': 'NSC', 'cloud_type': None}
        ],
        'weather': None
    }
}]