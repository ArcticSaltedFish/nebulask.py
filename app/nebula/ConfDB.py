import os


def parse_nebula_graphd_endpoint():
    ng_endpoints_str = os.environ.get(
        "NG_ENDPOINTS", "127.0.0.1:9669,").split(",")
    ng_endpoints = []
    for endpoint in ng_endpoints_str:
        if endpoint:
            parts = endpoint.split(":")  # we dont consider IPv6 now
            ng_endpoints.append((parts[0], int(parts[1])))
    return ng_endpoints
