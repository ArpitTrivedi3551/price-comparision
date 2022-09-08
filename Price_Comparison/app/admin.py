from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(Category,CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(Brand,BrandAdmin)

class RAMAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(RAM,RAMAdmin)

class InternalStorageAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(InternalStorage,InternalStorageAdmin)

class BatteryCapacityAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(BatteryCapacity,BatteryCapacityAdmin)

class ScreenSizeAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(ScreenSize,ScreenSizeAdmin)

class PrimaryRearCameraAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(PrimaryRearCamera,PrimaryRearCameraAdmin)

class FrontCameraAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(FrontCamera,FrontCameraAdmin)

class OperatingSystemAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(OperatingSystem,OperatingSystemAdmin)

class NetworkConnectivityAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(NetworkConnectivity,NetworkConnectivityAdmin)

class ProcessorSpeedAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(ProcessorSpeed,ProcessorSpeedAdmin)

class NumberOfCoresAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(NumberOfCores,NumberOfCoresAdmin)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(Availability,AvailabilityAdmin)

class Product_imgAdmin(admin.StackedInline):
    model = Product_img

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','Model','category','brand','RAM','InternalStorage','BatteryCapacity','ScreenSize','PrimaryRearCamera','FrontCamera','OperatingSystem','NetworkConnectivity','ProcessorSpeed','NumberOfCores','brand','Availability')
    inlines = [Product_imgAdmin]
admin.site.register(Product,ProductAdmin)


class SpecificationsAdmin(admin.ModelAdmin):
    list_display=('id','Model','Brand','Model_Name','Price_in_india','Release_Data','Dimensions','Weight','Battery_capacity','Fast_charging','Colours','Screen_Size','Touchscreen','Resolution','Protection_type','Aspect_ratio','Processor_make','RAM','Internal_storage','Rear_Camera','No_of_Rear_Cameras','Rear_autofocus','Rear_flash','Front_Camera','No_of_Front_Cameras','Operating_system','Skin','Wi_fi','GPS','Bluetooth','USB_Type_C','Number_of_SIMs','In_Display_Fingerprint_Sensor','Compass_Magnetometer','Proximity_sensor','Accelerometer','Ambient_light_sensor','Gyroscope')
admin.site.register(Specifications,SpecificationsAdmin)

class Product_imgAdmin(admin.ModelAdmin):
    list_display=('Model','image')
admin.site.register(Product_img,Product_imgAdmin)