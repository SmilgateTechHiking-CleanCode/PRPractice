package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.response.WidgetMetricResponse;
import org.springframework.stereotype.Service;

@Service
public class WidgetMetricServiceImpl implements WidgetMetricService {

    // private final WidgetMetricClient metricClient;
    @Override
    public WidgetMetricResponse getMetricData(String widgetId) {
        // return metricClient.getMetricData(widgetId);
        return null;
    }
}
