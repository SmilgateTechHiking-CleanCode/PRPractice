package com.refactoring.dashboard.api.controller;

import com.refactoring.dashboard.api.dto.request.WidgetDataRequest;
import com.refactoring.dashboard.api.dto.response.WidgetDataResponse;
import com.refactoring.dashboard.api.service.WidgetDataService;
import com.refactoring.dashboard.api.service.WidgetDataServiceExtractor;
import com.refactoring.dashboard.api.utils.enums.WidgetDataType;
import lombok.RequiredArgsConstructor;
import org.apache.coyote.BadRequestException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/v1/dashboards/widgets")
@RequiredArgsConstructor
public class WidgetDataController {

    @PutMapping
    public ResponseEntity<WidgetDataResponse> getEventData(@RequestBody WidgetDataRequest request) throws BadRequestException {

        WidgetDataType type = WidgetDataType.fromString(request.getType());
        if (type == WidgetDataType.UNKNOWN) {
            throw new BadRequestException("unknown widget type: " + request.getType());
        }

        WidgetDataService widgetDataService = WidgetDataServiceExtractor.get(type);

        return ResponseEntity.ok(widgetDataService.getData(request));
    }
}
