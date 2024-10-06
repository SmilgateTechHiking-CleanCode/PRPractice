package com.refactoring.dashboard.api.utils.enums;

public enum WidgetDataType {

    EVENT("event"),
    METRIC("metric"),
    GRID("grid"),

    UNKNOWN("");

    private String type;

    WidgetDataType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public static WidgetDataType fromString(String type) {
        for (WidgetDataType widgetDataType : WidgetDataType.values()) {
            if (widgetDataType.getType().equalsIgnoreCase(type)) {
                return widgetDataType;
            }
        }
        return UNKNOWN;
    }
}
