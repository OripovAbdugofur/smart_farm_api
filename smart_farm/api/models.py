from django.db import models


class Sensor(models.Model):
    SENSOR_TYPES = [
        ('temperature', 'Harorat'),
        ('humidity', 'Namlik'),
        ('soil_moisture', 'Tuproq namligi'),
        ('light', 'Yorug\'lik'),
    ]

    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPES)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_sensor_type_display()})"


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.sensor.name}: {self.value} at {self.timestamp}"


class Device(models.Model):
    DEVICE_TYPES = [
        ('pump', 'Nasos'),
        ('fan', 'Ventilyator'),
        ('light', 'Yoritgich'),
        ('heater', 'Isitgich'),
    ]

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_device_type_display()})"