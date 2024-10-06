package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.utils.enums.WidgetDataType;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class WidgetDataServiceExtractor {

    private static List<WidgetDataService> staticWidgetDataList;

    @Autowired
    private List<WidgetDataService> widgetDataList;


    public WidgetDataServiceExtractor(List<WidgetDataService> widgetDataList) {
        this.widgetDataList = widgetDataList;
    }

    public static WidgetDataService get(String type) {
        return staticWidgetDataList.stream().filter(widgetDataService -> widgetDataService.supports(type)).findFirst().orElseThrow(IllegalArgumentException::new);
    }

    public static WidgetDataService get(WidgetDataType type) {
        return staticWidgetDataList.stream().filter(widgetDataService -> widgetDataService.supports(type)).findFirst().orElseThrow(IllegalArgumentException::new);
    }

    @PostConstruct
    private void initialize() {
        staticWidgetDataList = this.widgetDataList;
    }
}
