from rest_framework import serializers

class PhoneListSerializer(serializers.Serializer):

    _status_display = {
        0: "New",
        1: "SUCCESS",
        2: "FAILURE",
        3: "Half_Filled",
        4: "Not_reachable",
        5: "Wrong_No",
        6: "Trash",
    }

    id = serializers.IntegerField()
    phone = serializers.CharField()
    status = serializers.IntegerField()
    statue_display = serializers.SerializerMethodField()

    def get_statue_display(self, obj):
        return self._status_display[obj.status]

class PhoneAddDataSerializer(serializers.Serializer):

    phone = serializers.CharField()


class PhoneUpdateDataSerializer(serializers.Serializer):

    status = serializers.IntegerField()