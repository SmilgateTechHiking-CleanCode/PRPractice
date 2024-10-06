package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.response.WidgetMetricResponse;

public interface WidgetMetricService {
    WidgetMetricResponse getMetricData(String widgetId);
}
