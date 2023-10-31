#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class Thickness(DressUpShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Thickness
                | 
                | Represents the thickness shape.
                | The thickness shape is made up of a collection of faces to process and an
                | offset parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.thickness = com_object

    @property
    def faces_to_thicken(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FacesToThicken() As References (Read Only)
                | 
                |     Returns the collection of faces to be thickened.
                | 
                |     Example:
                |         The following example returns in list the list of faces of the
                |         thickness firstThickness:
                | 
                |          Set list = firstThickness.FacesToThicken

        :rtype: References
        """

        return References(self.thickness.FacesToThicken)

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Offset() As Length (Read Only)
                | 
                |     Returns the thickness offset.
                | 
                |     Example:
                |         The following example returns in offset the offset of the thickness
                |         firstThickness:
                | 
                |          Set offset = firstThickness.Offset

        :rtype: Length
        """

        return Length(self.thickness.Offset)

    def add_face_to_thicken(self, i_face_to_thicken: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceToThicken(Reference iFaceToThicken)
                | 
                |     Adds a new face to be thickened.
                | 
                |     Parameters:
                | 
                |         iFaceToThicken
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example adds the new face face to thicken for the thickness
                |     firstThickness:
                | 
                |      call firstThickness.AddFaceToThicken(face)

        :param Reference i_face_to_thicken:
        :rtype: None
        """
        return self.thickness.AddFaceToThicken(i_face_to_thicken.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_to_thicken'
        # # vba_code = """
        # # Public Function add_face_to_thicken(thickness)
        # #     Dim iFaceToThicken (2)
        # #     thickness.AddFaceToThicken iFaceToThicken
        # #     add_face_to_thicken = iFaceToThicken
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_face_with_different_thickness(self, i_face_to_thicken: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceWithDifferentThickness(Reference
                | iFaceToThicken)
                | 
                |     Adds a new face to thicken with a different offset value.
                | 
                |     Parameters:
                | 
                |         iFaceToThicken
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example adds the new face face to thicken with a different
                |     offset value for the thickness firstThickness:
                | 
                |      call firstThickness.AddFaceWithDifferentThickness(face)

        :param Reference i_face_to_thicken:
        :rtype: None
        """
        return self.thickness.AddFaceWithDifferentThickness(i_face_to_thicken.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_with_different_thickness'
        # # vba_code = """
        # # Public Function add_face_with_different_thickness(thickness)
        # #     Dim iFaceToThicken (2)
        # #     thickness.AddFaceWithDifferentThickness iFaceToThicken
        # #     add_face_with_different_thickness = iFaceToThicken
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_face_with_different_thickness(self, i_face_to_remove: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveFaceWithDifferentThickness(Reference
                | iFaceToRemove)
                | 
                |     Removes an existing thickened face.
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The face to remove
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example removes the existing face thickened face from the
                |     thickness firstThickness:
                | 
                |      call

        :param Reference i_face_to_remove:
        :rtype: None
        """
        return self.thickness.RemoveFaceWithDifferentThickness(i_face_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_face_with_different_thickness'
        # # vba_code = """
        # # Public Function remove_face_with_different_thickness(thickness)
        # #     Dim iFaceToRemove (2)
        # #     thickness.RemoveFaceWithDifferentThickness iFaceToRemove
        # #     remove_face_with_different_thickness = iFaceToRemove
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_volume_support(self, i_volume_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetVolumeSupport(Reference iVolumeSupport)
                | 
                |     Set support of Thickness feature.

        :param Reference i_volume_support:
        :rtype: None
        """
        return self.thickness.SetVolumeSupport(i_volume_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_volume_support'
        # # vba_code = """
        # # Public Function set_volume_support(thickness)
        # #     Dim iVolumeSupport (2)
        # #     thickness.SetVolumeSupport iVolumeSupport
        # #     set_volume_support = iVolumeSupport
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_face_to_thicken(self, i_face_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawFaceToThicken(Reference iFaceToWithdraw)
                | 
                |     Withdraws an existing thickened face.
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example withdraws the existing face thickened face from the
                |     thickness firstThickness:
                | 
                |      call firstThickness.WithdrawFaceToThicken(face)

        :param Reference i_face_to_withdraw:
        :rtype: None
        """
        return self.thickness.WithdrawFaceToThicken(i_face_to_withdraw.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_face_to_thicken'
        # # vba_code = """
        # # Public Function withdraw_face_to_thicken(thickness)
        # #     Dim iFaceToWithdraw (2)
        # #     thickness.WithdrawFaceToThicken iFaceToWithdraw
        # #     withdraw_face_to_thicken = iFaceToWithdraw
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Thickness(name="{self.name}")'
