package com.refactoring.dashboard.api.controller;

import com.refactoring.dashboard.api.dto.response.WidgetEnvetResponse;
import com.refactoring.dashboard.api.service.WidgetEventService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/v1/dashboards/widgets")
@RequiredArgsConstructor
public class WidgetEnvetController {

    private final WidgetEventService widgetEventService;

    @PutMapping("{widgetId}/events")
    public ResponseEntity<WidgetEnvetResponse> getEventData(@PathVariable("widgetId") String widgetId) {
        return ResponseEntity.ok(widgetEventService.getEventData(widgetId));
    }
}
