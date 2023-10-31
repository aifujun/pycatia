#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_grr_comp import SchGRRComp
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchCompGraphic(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchCompGraphic
                | 
                | Manage the graphical representation of a schematic component.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_comp_graphic = com_object

    def activate(self, i_grr_name: str, i_db2_where_at: tuple, o_grr: SchGRRComp) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Activate(CATBSTR iGRRName,
                | CATSafeArrayVariant iDb2WhereAt,
                | SchGRRComp oGRR)
                | 
                |     To add a new image to an existing object. This new image is an instance of
                |     graphical representation with the input name.
                | 
                |     Parameters:
                | 
                |         iGRRName
                |             The name of the graphic representation 
                |         iDb2WhereAt
                |             The x-y coordinates of the image position. If NULL, the image will
                |             be positioned at the origin. 
                |         oGRR
                |             Pointer to the new graphical image of the component.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchCompGraphic
                |          Dim strVar1 As String
                |          Dim dbVar2(2) As CATSafeArrayVariant
                |          Dim objArg3 As SchGRRComp
                |           ...
                |          objThisIntf.ActivatestrVar1,dbVar2,objArg3

        :param str i_grr_name:
        :param tuple i_db2_where_at:
        :param SchGRRComp o_grr:
        :rtype: tuple
        """
        return self.sch_comp_graphic.Activate(i_grr_name, i_db2_where_at, o_grr.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'activate'
        # # vba_code = """
        # # Public Function activate(sch_comp_graphic)
        # #     Dim iGRRName (2)
        # #     sch_comp_graphic.Activate iGRRName
        # #     activate = iGRRName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_graphical_representation(self, i_grr_to_add: SchGRRComp) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddGraphicalRepresentation(SchGRRComp iGRRToAdd)
                | 
                |     Add a graphical representation to a component.
                | 
                |     Parameters:
                | 
                |         iGRRToAdd
                |             The graphical representation to be added to the component.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchCompGraphic
                |          Dim objArg1 As SchGRRComp
                |           ...
                |          objThisIntf.AddGraphicalRepresentationobjArg1

        :param SchGRRComp i_grr_to_add:
        :rtype: None
        """
        return self.sch_comp_graphic.AddGraphicalRepresentation(i_grr_to_add.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_graphical_representation'
        # # vba_code = """
        # # Public Function add_graphical_representation(sch_comp_graphic)
        # #     Dim iGRRToAdd (2)
        # #     sch_comp_graphic.AddGraphicalRepresentation iGRRToAdd
        # #     add_graphical_representation = iGRRToAdd
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def deactivate(self, i_grr: SchGRRComp) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Deactivate(SchGRRComp iGRR)
                | 
                |     To remove an image to an existing object.
                | 
                |     Parameters:
                | 
                |         iGRR
                |             The graphical image to be removed from the component.
                |             
                |         iDb2WhereAt
                |             The x-y coordinates of the image position. If NULL, the image will
                |             be positioned at the origin. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchCompGraphic
                |          Dim objArg1 As SchGRRComp
                |           ...
                |          objThisIntf.DeactivateobjArg1

        :param SchGRRComp i_grr:
        :rtype: None
        """
        return self.sch_comp_graphic.Deactivate(i_grr.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'deactivate'
        # # vba_code = """
        # # Public Function deactivate(sch_comp_graphic)
        # #     Dim iGRR (2)
        # #     sch_comp_graphic.Deactivate iGRR
        # #     deactivate = iGRR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_graphical_images(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListGraphicalImages() As SchListOfObjects
                | 
                |     List all graphical images (instances of the rep) of a
                |     component.
                | 
                |     Parameters:
                | 
                |         oLGRR
                |             A list of graphical images (members are CATISchGRRComp interface
                |             pointers). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCompGraphic
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.ListGraphicalImages

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_comp_graphic.ListGraphicalImages())

    def list_graphical_representations(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListGraphicalRepresentations() As SchListOfObjects
                | 
                |     List all graphical representation of a component.
                | 
                |     Parameters:
                | 
                |         oLGRR
                |             A list of graphical representations (members are CATISchGRRComp
                |             interface pointers). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCompGraphic
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.ListGraphicalRepresentations

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_comp_graphic.ListGraphicalRepresentations())

    def remove_graphical_representation(self, i_grr_to_remove: SchGRRComp) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveGraphicalRepresentation(SchGRRComp iGRRToRemove)
                | 
                |     Remove a graphical representation from a component.
                | 
                |     Parameters:
                | 
                |         iGRRToRemove
                |             The graphical representation to be removed from the component.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchCompGraphic
                |          Dim objArg1 As SchGRRComp
                |           ...
                |          objThisIntf.RemoveGraphicalRepresentationobjArg1

        :param SchGRRComp i_grr_to_remove:
        :rtype: None
        """
        return self.sch_comp_graphic.RemoveGraphicalRepresentation(i_grr_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_graphical_representation'
        # # vba_code = """
        # # Public Function remove_graphical_representation(sch_comp_graphic)
        # #     Dim iGRRToRemove (2)
        # #     sch_comp_graphic.RemoveGraphicalRepresentation iGRRToRemove
        # #     remove_graphical_representation = iGRRToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def switch(self, i_grr: SchGRRComp, i_grr_name: str, o_grr: SchGRRComp) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Switch(SchGRRComp iGRR,
                | CATBSTR iGRRName,
                | SchGRRComp oGRR)
                | 
                |     Replace the input image object with an image of the graphical
                |     representation with the input name.
                | 
                |     Parameters:
                | 
                |         iGRR
                |             Pointer to the component graphical image to be switched.
                |             
                |         oGRR
                |             Pointer to the new graphical image of the component.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchCompGraphic
                |          Dim objArg1 As SchGRRComp
                |          Dim strVar2 As String
                |          Dim objArg3 As SchGRRComp
                |           ...
                |          objThisIntf.SwitchobjArg1,strVar2,objArg3

        :param SchGRRComp i_grr:
        :param str i_grr_name:
        :param SchGRRComp o_grr:
        :rtype: None
        """
        return self.sch_comp_graphic.Switch(i_grr.com_object, i_grr_name, o_grr.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'switch'
        # # vba_code = """
        # # Public Function switch(sch_comp_graphic)
        # #     Dim iGRR (2)
        # #     sch_comp_graphic.Switch iGRR
        # #     switch = iGRR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def switch_all(self, i_grr_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SwitchAll(CATBSTR iGRRName)
                | 
                |     Replace all occurances of the images of this component with those of the
                |     graphical representation with the input name.
                | 
                |     Parameters:
                | 
                |         iGRRName
                |             The name of the graphical representation 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCompGraphic
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.SwitchAllstrVar1

        :param str i_grr_name:
        :rtype: None
        """
        return self.sch_comp_graphic.SwitchAll(i_grr_name)

    def __repr__(self):
        return f'SchCompGraphic(name="{self.name}")'
