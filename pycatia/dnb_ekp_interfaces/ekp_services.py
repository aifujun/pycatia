#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.system_interfaces.any_object import AnyObject


class EkpServices(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     EKPServices
                | 
                | Interface to assign and remove Engineering Requirements to and from an
                | activity.
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ekp_services = com_object

    def assign_er(self, i_geometric_feature: AnyObject, i_fta: AnyObject, i_operation: Activity, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AssignER(CATBaseDispatch iGeometricFeature,
                | CATBaseDispatch iFTA,
                | Activity iOperation,
                | ItemAssignmentType iType)
                | 
                |     Assigns the passed geometric feature to the operation.
                | 
                |     Parameters:
                | 
                |         iGeometricFeature
                |             [in] Geometric Element user wants to assign User has a handle to
                |             this object 
                |         iFTA
                |             [in] Underlying FTA object associated with the geometric feature
                |             Can be obtained using CAA C++ API exposed by CATIA FTA Modeler and passed to
                |             this API 
                |         iOperation
                |             [in] The Operation to which assignment needs to be done User has a
                |             handle to this object 
                |         iType
                |             [in] Type of assignment whether ‘Partial’ or ‘Complete’ User needs
                |             to know what type of assignment he/she wants to
                |             make

        :param AnyObject i_geometric_feature:
        :param AnyObject i_fta:
        :param Activity i_operation:
        :param int i_type: enum item_assignment_type
        :rtype: None
        """
        return self.ekp_services.AssignER(
            i_geometric_feature.com_object,
            i_fta.com_object,
            i_operation.com_object,
            i_type
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'assign_er'
        # # vba_code = """
        # # Public Function assign_er(ekp_services)
        # #     Dim iGeometricFeature (2)
        # #     ekp_services.AssignER iGeometricFeature
        # #     assign_er = iGeometricFeature
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def assign_er_with_fta(self, i_fta: AnyObject, i_operation: Activity, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AssignERWithFTA(CATBaseDispatch iFTA,
                | Activity iOperation,
                | ItemAssignmentType iType)
                | 
                |     Assigns the passed FTA to the Operation .
                | 
                |     Parameters:
                | 
                |         iFTA
                |             [in] FTA to be passed 
                |         iOperation
                |             [in] The Operation to which assignment needs to be done
                |             
                |         iType
                |             [in] type of assignment - partial or complete

        :param AnyObject i_fta:
        :param Activity i_operation:
        :param int i_type: enum item_assignment_type
        :rtype: None
        """
        return self.ekp_services.AssignERWithFTA(i_fta.com_object, i_operation.com_object, i_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'assign_er_with_fta'
        # # vba_code = """
        # # Public Function assign_er_with_fta(ekp_services)
        # #     Dim iFTA (2)
        # #     ekp_services.AssignERWithFTA iFTA
        # #     assign_er_with_fta = iFTA
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_assigned_er(self, i_operation: Activity, i_type: int, o_item_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAssignedER(Activity iOperation,
                | ItemAssignmentType iType,
                | CATSafeArrayVariant oItemList)
                | 
                |     Given a type of assignment, this method returns all the ER assigned to the
                |     Operation.
                | 
                |     Parameters:
                | 
                |         iOperation
                |             [in] The Operation to which assignment needs to be done
                |             
                |         iType
                |             [in] the type of assignment, it could be partial or complete
                |             
                |         oItemList
                |             [out] List of assigned ERs to the operation or
                |             activity

        :param Activity i_operation:
        :param int i_type: enum item_assignment_type
        :param tuple o_item_list:
        :rtype: None
        """
        return self.ekp_services.GetAssignedER(i_operation.com_object, i_type, o_item_list)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_assigned_er'
        # # vba_code = """
        # # Public Function get_assigned_er(ekp_services)
        # #     Dim iOperation (2)
        # #     ekp_services.GetAssignedER iOperation
        # #     get_assigned_er = iOperation
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_er_assignment(
            self,
            i_geometric_feature: AnyObject,
            i_fta: AnyObject,
            i_operation: Activity,
            i_type: int
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveERAssignment(CATBaseDispatch iGeometricFeature,
                | CATBaseDispatch iFTA,
                | Activity iOperation,
                | ItemAssignmentType iType)
                | 
                |     Removes the ER assignment for the passed Geometric
                |     Feature.
                | 
                |     Parameters:
                | 
                |         iGeometricFeature
                |             [in] The Geometric feature which will be unassigned
                |             
                |         iFTA
                |             [in] FTA to be passed 
                |         iOperation
                |             [in] The Operation to which assignment needs to be done
                |             
                |         iType
                |             [in] the type of assignment, it could be partial or
                |             complete

        :param AnyObject i_geometric_feature:
        :param AnyObject i_fta:
        :param Activity i_operation:
        :param int i_type: enum item_assignment_type
        :rtype: None
        """
        return self.ekp_services.RemoveERAssignment(
            i_geometric_feature.com_object,
            i_fta.com_object,
            i_operation.com_object,
            i_type
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_er_assignment'
        # # vba_code = """
        # # Public Function remove_er_assignment(ekp_services)
        # #     Dim iGeometricFeature (2)
        # #     ekp_services.RemoveERAssignment iGeometricFeature
        # #     remove_er_assignment = iGeometricFeature
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_er_with_fta(self, i_fta: AnyObject, i_operation: Activity, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveERWithFTA(CATBaseDispatch iFTA,
                | Activity iOperation,
                | ItemAssignmentType iType)
                | 
                |     Removes the ER assignment for the passed FTA.
                | 
                |     Parameters:
                | 
                |         iFTA
                |             [in] the FTA to be passed to the operation 
                |         iOperation
                |             [in] The Operation to which assignment needs to be done
                |             
                |         iType
                |             [in] the type of assignment - partial or complete

        :param AnyObject i_fta:
        :param Activity i_operation:
        :param int i_type: enum item_assignment_type
        :rtype: None
        """
        return self.ekp_services.RemoveERWithFTA(i_fta.com_object, i_operation.com_object, i_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_er_with_fta'
        # # vba_code = """
        # # Public Function remove_er_with_fta(ekp_services)
        # #     Dim iFTA (2)
        # #     ekp_services.RemoveERWithFTA iFTA
        # #     remove_er_with_fta = iFTA
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'EkpServices(name="{self.name}")'
