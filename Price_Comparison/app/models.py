from django.db import models
from django.utils.html import mark_safe


# Create your models here.
# Category
class Category(models.Model):
    title=models.CharField(max_length=100)
    # image=models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural='01. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="Brand_img/")

    class Meta:
        verbose_name_plural='02. Brands'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class RAM(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='03. RAM'

    def __str__(self):
        return self.title

class InternalStorage(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='04. Internal Storage'

    def __str__(self):
        return self.title

class BatteryCapacity(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='05. Battery Capacity'

    def __str__(self):
        return self.title

class ScreenSize(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='06. Screen Size'

    def __str__(self):
        return self.title

class PrimaryRearCamera(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='07. Primary Rear Camera'

    def __str__(self):
        return self.title

class FrontCamera(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='08. Front Camera'

    def __str__(self):
        return self.title

class OperatingSystem(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='09. Operating System'

    def __str__(self):
        return self.title

class NetworkConnectivity(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='10. Network Connectivity'

    def __str__(self):
        return self.title

class ProcessorSpeed(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='11. Processor Speed'

    def __str__(self):
        return self.title

class NumberOfCores(models.Model):
    title=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural='12. Number Of Cores'

    def __str__(self):
        return self.title

class Availability(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural='13. Availability'

    def __str__(self):
        return self.title

class Product(models.Model):
    Model=models.CharField(max_length=200)
    Thumbnail=models.ImageField(upload_to="Mobile_img/",blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE ,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True)
    RAM=models.ForeignKey(RAM,on_delete=models.CASCADE,blank=True)
    InternalStorage=models.ForeignKey(InternalStorage,on_delete=models.CASCADE,blank=True)
    BatteryCapacity=models.ForeignKey(BatteryCapacity,on_delete=models.CASCADE,blank=True)
    ScreenSize=models.ForeignKey(ScreenSize,on_delete=models.CASCADE,blank=True)
    PrimaryRearCamera=models.ForeignKey(PrimaryRearCamera,on_delete=models.CASCADE,blank=True)
    FrontCamera=models.ForeignKey(FrontCamera,on_delete=models.CASCADE,blank=True)
    OperatingSystem=models.ForeignKey(OperatingSystem,on_delete=models.CASCADE,blank=True)
    NetworkConnectivity=models.ForeignKey(NetworkConnectivity,on_delete=models.CASCADE,blank=True)
    ProcessorSpeed=models.ForeignKey(ProcessorSpeed,on_delete=models.CASCADE,blank=True)
    NumberOfCores=models.ForeignKey(NumberOfCores,on_delete=models.CASCADE,blank=True)
    Availability=models.ForeignKey(Availability,on_delete=models.CASCADE,blank=True)
    class Meta:
        verbose_name_plural='13. Product'
 
    def __str__(self):
        return self.Model

class Product_img(models.Model):
    Model = models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.FileField(upload_to="Product_img/")
    def __str__(self):
        return self.Model.Model


class Specifications(models.Model):
    Model = models.ForeignKey(Product,on_delete=models.CASCADE ,blank=True)
    Brand=models.CharField(max_length=50)
    Model_Name = models.CharField(max_length=50)
    Price_in_india = models.IntegerField()
    Release_Data = models.CharField(max_length=50)
    Dimensions = models.CharField(max_length=50)
    Weight = models.CharField(max_length=50)
    Battery_capacity = models.IntegerField()
    Fast_charging = models.CharField(max_length=50)
    Colours = models.CharField(max_length=50)
    Screen_Size = models.DecimalField(max_digits=5,decimal_places=2)
    Touchscreen = models.CharField(max_length=5)
    Resolution = models.CharField(max_length=20)
    Protection_type = models.CharField(max_length=20)
    Aspect_ratio = models.CharField(max_length=20)
    Processor_make = models.CharField(max_length=50)
    Processor_Core = models.CharField(max_length=50)
    RAM = models.CharField(max_length=5)
    Internal_storage = models.CharField(max_length=10)
    Rear_Camera = models.CharField(max_length=200)
    No_of_Rear_Cameras = models.IntegerField()
    Rear_autofocus = models.CharField(max_length=5)
    Rear_flash = models.CharField(max_length=5)
    Front_Camera = models.CharField(max_length=200)
    No_of_Front_Cameras = models.IntegerField()
    Operating_system = models.CharField(max_length=50)
    Skin = models.CharField(max_length=50)
    Wi_fi = models.CharField(max_length=5)
    GPS = models.CharField(max_length=5)
    Bluetooth = models.CharField(max_length=20)
    USB_Type_C = models.CharField(max_length=5)
    Number_of_SIMs = models.IntegerField()
    Sim_Type = models.CharField(max_length=50)
    GSM_CDMA = models.CharField(max_length=5)
    ThreeG = models.CharField(max_length=5)
    FourG = models.CharField(max_length=5)
    FiveG = models.CharField(max_length=5)

    In_Display_Fingerprint_Sensor = models.CharField(max_length=5)
    Compass_Magnetometer =models.CharField(max_length=5)
    Proximity_sensor =models.CharField(max_length=5)
    Accelerometer =models.CharField(max_length=5)
    Ambient_light_sensor =models.CharField(max_length=5)
    Gyroscope =models.CharField(max_length=5)
    class Meta:
        verbose_name_plural='13. Specifications'

    def __str__(self):
        return self.Model_Name

    