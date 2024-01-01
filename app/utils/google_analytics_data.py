import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Metric,
    RunReportRequest,
)
from config.config import BaseConfig

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = BaseConfig.KEYS_LOCATION

client = BetaAnalyticsDataClient()

def get_google_analytics_data(property_id, metric_name):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[],
        metrics=[
            Metric(name=metric_name)
        ],
        date_ranges=[DateRange(
            start_date="2020-01-01",
            end_date="today"
        )],
    )
    response = client.run_report(request)

    formatted_response = {
        'metric_headers': [],
        'rows': [],
        'row_count': response.row_count,
        'metadata': {
            'currency_code': response.metadata.currency_code,
            'time_zone': response.metadata.time_zone
        },
        'kind': response.kind
    }

    for metric_header in response.metric_headers:
        formatted_response['metric_headers'].append({
            'name': metric_header.name,
            'type': metric_header.type_.name
        })

    for row in response.rows:
        row_values = []
        for metric_value in row.metric_values:
            row_values.append({'value': metric_value.value})
        formatted_response['rows'].append({'metric_values': row_values})

    processed_data = {}
    if formatted_response['rows']:
        for i, metric_header in enumerate(formatted_response['metric_headers']):
            metric_name = metric_header['name']
            metric_value = formatted_response['rows'][0]['metric_values'][i]['value']
            processed_data[metric_name] = metric_value

    return processed_data