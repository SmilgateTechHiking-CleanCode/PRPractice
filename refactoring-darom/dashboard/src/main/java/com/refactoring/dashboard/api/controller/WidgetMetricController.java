package com.refactoring.dashboard.api.controller;

import com.refactoring.dashboard.api.dto.response.WidgetMetricResponse;
import com.refactoring.dashboard.api.service.WidgetMetricService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/v1/dashboards/widgets/metric")
@RequiredArgsConstructor
public class WidgetMetricController {

    private final WidgetMetricService widgetMetricService;

    @PutMapping("{widgetId}/metrics")
    public ResponseEntity<WidgetMetricResponse> getEventData(@PathVariable("widgetId") String widgetId) {
        return ResponseEntity.ok(widgetMetricService.getMetricData(widgetId));
    }
}
