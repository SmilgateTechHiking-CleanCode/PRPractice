package com.refactoring.dashboard.api.controller;

import com.refactoring.dashboard.api.dto.response.WidgetGridResponse;
import com.refactoring.dashboard.api.service.WidgetGridService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/v1/dashboards/widgets/grid")
@RequiredArgsConstructor
public class WidgetGridController {

    private final WidgetGridService widgetGridService;

    @PutMapping("/releases")
    public ResponseEntity<WidgetGridResponse> getEventData(@PathVariable("widgetId") String widgetId) {
        return ResponseEntity.ok(widgetGridService.getGridData(widgetId));
    }
}
