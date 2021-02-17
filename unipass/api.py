import os
from typing import TypedDict
import xml.etree.ElementTree as ET

import httpx

UNIPASS_URL = "https://unipass.customs.go.kr:38010/ext/"
UNIPASS_URL_REST = f"{UNIPASS_URL}rest/"


class UP002Resp1Detail(TypedDict):
    shpmPckUt: str  # 선(기)적포장단위
    shpmWght: str  # 선적중량
    tkofDt: str  # 출항일자
    shpmPckGcnt: str  # 선(기)적포장개수
    blNo: str  # b/l번호


class UP002Resp1(TypedDict):
    mnurConm: str  # 선(기)적포장단위
    acptDt: str  # 제조자상호
    exppnConm: str  # 선적완료여부
    loadDtyTmlm: str  # 수리일자
    sanm: str  # 수리일시
    acptDttm: str  # 선적중량
    shpmPckGcnt: str  # 수출자상호
    csclPckUt: str  # 적재의무기한
    shpmPckUt: str  # 선박/편명
    shpmCmplYn: str  # 수출신고번호
    shpmWght: str  # 통관중량
    expDclrNo: str  # 선(기)적포장개수
    csclWght: str  # 통관포장단위
    csclPckGcnt: str  # 통관포장개수
    details: list[UP002Resp1Detail]  # 상세


def api002(api_key: str, exp_dclr_no: str) -> UP002Resp1:
    """
    수출신고번호별 수출이행 내역 (수출신고번호로 조회)

    :param api_key: unipass 의 수출신고번호별수출이행내역조회 인증키
    :param exp_dclr_no: 수출신고번호
    :return:
    """
    url = f"{UNIPASS_URL_REST}expDclrNoPrExpFfmnBrkdQry/" \
          f"retrieveExpDclrNoPrExpFfmnBrkd"
    params = {'crkyCn': api_key, 'expDclrNo': exp_dclr_no, 'blYy': ''}
    resp = httpx.get(url, params=params)
    tree = ET.fromstring(resp.text)
    xml = tree.find('expDclrNoPrExpFfmnBrkdQryRsltVo')
    keys = ['mnurConm', 'acptDt', 'exppnConm', 'loadDtyTmlm', 'sanm',
            'acptDttm', 'shpmPckGcnt', 'csclPckUt', 'shpmPckUt',
            'shpmCmplYn', 'shpmWght', 'expDclrNo', 'csclWght', 'csclPckGcnt', ]
    result: UP002Resp1 = {}
    for key in keys:
        result[key] = xml.find(key).text
    details: list[UP002Resp1Detail] = []

    keys = ['shpmPckUt', 'shpmWght', 'tkofDt', 'shpmPckGcnt', 'blNo', ]

    for detail_xml in tree.findall('expDclrNoPrExpFfmnBrkdDtlQryRsltVo'):
        detail: UP002Resp1Detail = {}
        for key in keys:
            detail[key] = detail_xml.find(key).text
        details.append(detail)

    result['details'] = details

    return result
