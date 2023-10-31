#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_doubles import SchListOfDoubles
from pycatia.system_interfaces.any_object import AnyObject


class SchCompGroupExt(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchCompGroupExt
                | 
                | Manage the graphical representation of a temporary group of schematic
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_comp_group_ext = com_object

    def get_placement_axis(self, o_db6_place_matrix: SchListOfDoubles) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPlacementAxis(SchListOfDoubles oDb6PlaceMatrix)
                | 
                |     Get the placement axis for the component group.
                | 
                |     Parameters:
                | 
                |         oDb6PlaceMatrix
                |             Placement matrix of the component group (an array of 6 doubles) See
                |             
                |         SchGRRComp.GetTransformation2D for explanation of this argument.
                |         
                |     Example:
                |
                |          Dim objThisIntf As SchCompGroupExt
                |          Dim objArg1 As SchListOfDoubles
                |           ...
                |          objThisIntf.GetPlacementAxisobjArg1

        :param SchListOfDoubles o_db6_place_matrix:
        :rtype: None
        """
        return self.sch_comp_group_ext.GetPlacementAxis(o_db6_place_matrix.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_placement_axis'
        # # vba_code = """
        # # Public Function get_placement_axis(sch_comp_group_ext)
        # #     Dim oDb6PlaceMatrix (2)
        # #     sch_comp_group_ext.GetPlacementAxis oDb6PlaceMatrix
        # #     get_placement_axis = oDb6PlaceMatrix
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_placement_axis(self, o_db6_place_matrix: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPlacementAxis(CATSafeArrayVariant oDb6PlaceMatrix)
                | 
                |     Set the placement axis for the component group.
                | 
                |     Parameters:
                | 
                |         iDb6PlaceMatrix
                |             Placement matrix of the component group (an array of 6 doubles) See
                |             
                | 
                |         SchGRRComp.GetTransformation2D for explanation of this argument.
                |         
                |     Example:
                |
                |          Dim objThisIntf As SchCompGroupExt
                |          Dim dbVar1(x) As CATSafeArrayVariant
                |           ...
                |          objThisIntf.SetPlacementAxisdbVar1

        :param tuple o_db6_place_matrix:
        :rtype: tuple
        """
        return self.sch_comp_group_ext.SetPlacementAxis(o_db6_place_matrix)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_placement_axis'
        # # vba_code = """
        # # Public Function set_placement_axis(sch_comp_group_ext)
        # #     Dim oDb6PlaceMatrix (2)
        # #     sch_comp_group_ext.SetPlacementAxis oDb6PlaceMatrix
        # #     set_placement_axis = oDb6PlaceMatrix
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchCompGroupExt(name="{self.name}")'
