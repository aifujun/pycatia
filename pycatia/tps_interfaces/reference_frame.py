#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.tps_interfaces.annotations import Annotations
from pycatia.tps_interfaces.user_surface import UserSurface
from pycatia.types import cat_variant


class ReferenceFrame(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ReferenceFrame
                | 
                | Interface designed to manage reference frame associated to a
                | TPS.
                | Reference frame is composed of three boxes.
                | 
                |                          Reference Frame
                |                         / 
                |                   _____|_____
                |                  /           \
                |          ---------------------
                |          |   |   |Box|Box|Box|
                |          |   |   | 1 | 2 | 3 |
                |          ---------------------
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.reference_frame = com_object

    @property
    def all_datums_simple(self) -> Annotations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AllDatumsSimple() As Annotations (Read Only)
                | 
                | 
                |   
                | 
                |      Retrieves all datums simple used in Reference Frame.
                |        
                | 
                | 
                |       
                |      Parameters:
                |       
                | 
                |             
                | 
                | 
                |             
                |          opiListDatumsSimple
                |            
                |                  All objects of the collection

        :return: Annotations
        :rtype: Annotations
        """

        return Annotations(self.reference_frame.AllDatumsSimple)

    def frame(self, o_first_box: str, o_second_box: str, o_third_box: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Frame(CATBSTR oFirstBox,
                | CATBSTR oSecondBox,
                | CATBSTR oThirdBox)
                | 
                | 
                |   
                | 
                |      Retrieves Frame of the TPS.
                |        
                | 
                | 
                |       
                |      Parameters:
                |       
                | 
                |             
                | 
                | 
                |             
                |          oFirstBox
                |            
                |                
                |             
                |          oSecondBox
                |            
                |                
                |             
                |          oThirdBox
                |            
                |                  Texts in first, second and third boxes.

        :param str o_first_box:
        :param str o_second_box:
        :param str o_third_box:
        :return: None
        :rtype: None
        """
        return self.reference_frame.Frame(o_first_box, o_second_box, o_third_box)

    def get_axis_system_ttrs(self, op_axis_system_ttrs: UserSurface) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAxisSystemTTRS(UserSurface opAxisSystemTTRS)
                | 
                | 
                |   
                | 
                |      Gets the AxisSystem TTRS.
                |       
                | 
                | 
                |       
                |      Parameters:
                |       
                | 
                |             
                | 
                | 
                |             
                |          opAxisSystemTTRS
                |            
                |                AxisSystem TTRS
                |               
                | 
                | 
                |           
                |      Returns: 
                |       
                |           HRESULT   S_OK:- the Axis System has been correctly
                |           retrieved.
                |            E_FAIL or E_NOIMPL : Axis System cannot be retrieved.

        :param UserSurface op_axis_system_ttrs:
        :return: None
        :rtype: None
        """
        return self.reference_frame.GetAxisSystemTTRS(op_axis_system_ttrs.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_axis_system_ttrs'
        # # vba_code = """
        # # Public Function get_axis_system_ttrs(reference_frame)
        # #     Dim opAxisSystemTTRS (2)
        # #     reference_frame.GetAxisSystemTTRS opAxisSystemTTRS
        # #     get_axis_system_ttrs = opAxisSystemTTRS
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_degrees_of_freedom(self, in_box: cat_variant, o_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDegreesOfFreedom(CATVariant inBox,
                | CATBSTR oValue)
                | 
                | 
                |   
                | 
                |      Retrieves the values of Degrees Of Freedom(DOF)
                |      [x,y,z,u,v,w].
                |      Is only defined when "Axis System" attribute is valued.
                |      Only for ASME 2009 (does not exist in ISO).
                |       
                | 
                | 
                |       
                |      Parameters:
                |       
                | 
                |             
                | 
                | 
                |             
                |          inBox
                |            
                |                First, Second or the Third Box of the DRF on
                |                which
                |                the Degrees Of Freedom is to be retrieved.
                |               
                |             
                |          oValue
                |            
                |                oValue begins with the symbol :”[“ and ends by the symbol
                |                “]”.
                |                and between these symbols “[..]”, value are a a combination
                |                of
                |                following legal values:
                |                x,
                |                y,
                |                z,
                |                u,
                |                v,
                |                w
                |               
                | 
                | 
                |           
                |      Returns: 
                |       
                |           HRESULT    S_OK : the Degrees Of Freedom has been correctly retrieved.
                |             E_FAIL or E_NOIMPL : the Degrees Of Freedom cannot be retrieved.

        :param CATVariant in_box:
        :param str o_value:
        :return: None
        :rtype: None
        """
        return self.reference_frame.GetDegreesOfFreedom(in_box.com_object, o_value)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_degrees_of_freedom'
        # # vba_code = """
        # # Public Function get_degrees_of_freedom(reference_frame)
        # #     Dim inBox (2)
        # #     reference_frame.GetDegreesOfFreedom inBox
        # #     get_degrees_of_freedom = inBox
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_axis_system_ttrs(self, ip_axis_system_ttrs: UserSurface) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAxisSystemTTRS(UserSurface ipAxisSystemTTRS)
                | 
                | 
                |   
                | 
                |      Sets the AxisSystem TTRS.
                |       
                | 
                | 
                |       
                |      Parameters:
                |       
                | 
                |             
                | 
                | 
                |             
                |          ipAxisSystemTTRS
                |            
                |                AxisSystem TTRS. If it is NULL, the AxisSystem TTRS in the
                |                model
                |                will be removed.
                |               
                | 
                | 
                |           
                |      Returns: 
                |       
                |           HRESULT   S_OK:- the Axis System has been correctly
                |           set.
                |            E_FAIL or E_NOIMPL : Axis System cannot be set.

        :param UserSurface ip_axis_system_ttrs:
        :return: None
        :rtype: None
        """
        return self.reference_frame.SetAxisSystemTTRS(ip_axis_system_ttrs.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_axis_system_ttrs'
        # # vba_code = """
        # # Public Function set_axis_system_ttrs(reference_frame)
        # #     Dim ipAxisSystemTTRS (2)
        # #     reference_frame.SetAxisSystemTTRS ipAxisSystemTTRS
        # #     set_axis_system_ttrs = ipAxisSystemTTRS
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_degrees_of_freedom(self, in_box: cat_variant, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDegreesOfFreedom(CATVariant inBox,
                | CATBSTR iValue)
                | 
                | 
                |   
                | 
                |      Sets the values of Degrees Of Freedom(DOF) [x,y,z,u,v,w].
                |      Is only defined when "Axis System" attribute is valued.
                |      Only for ASME 2009 (does not exist in ISO).
                |       
                | 
                | 
                |       
                |      Parameters:
                |       
                | 
                |             
                | 
                | 
                |             
                |          inBox
                |            
                |                First, Second or the Third Box of the DRF on
                |                which
                |                the Degrees Of Freedom is to be set.
                |               
                |             
                |          iValue
                |            
                |                iValue must begin by the symbol :”[“ and must end by the symbol
                |                “]”.
                |                and between these symbols “[..]”, value must be a combination
                |                of
                |                following legal values:
                |                x,
                |                y,
                |                z,
                |                u,
                |                v,
                |                w
                |                E.G.1:- To set [x,z] as the DOF:-
                |                               iValue = [x,z];
                |                E.G.2:- To set [y] as the DOF:-
                |                               iValue = [y];
                |               
                | 
                | 
                |           
                |      Returns: 
                |       
                |           HRESULT    S_OK : the Degrees Of Freedom has been correctly set.
                |             E_FAIL or E_NOIMPL : the Degrees Of Freedom cannot be set.

        :param CATVariant in_box:
        :param str i_value:
        :return: None
        :rtype: None
        """
        return self.reference_frame.SetDegreesOfFreedom(in_box.com_object, i_value)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_degrees_of_freedom'
        # # vba_code = """
        # # Public Function set_degrees_of_freedom(reference_frame)
        # #     Dim inBox (2)
        # #     reference_frame.SetDegreesOfFreedom inBox
        # #     set_degrees_of_freedom = inBox
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_frame(self, i_first_box: str, i_second_box: str, i_third_box: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFrame(CATBSTR iFirstBox,
                | CATBSTR iSecondBox,
                | CATBSTR iThirdBox)
                | 
                | 
                |   
                | 
                |      Set Frame of the TPS.
                |        
                | 
                | 
                |       
                |      Parameters:
                |       
                | 
                |             
                | 
                | 
                |             
                |          oFirstBox
                |            
                |                
                |             
                |          oSecondBox
                |            
                |                
                |             
                |          oThirdBox
                |            
                |                  Texts in first, second and third boxes.

        :param str i_first_box:
        :param str i_second_box:
        :param str i_third_box:
        :return: None
        :rtype: None
        """
        return self.reference_frame.SetFrame(i_first_box, i_second_box, i_third_box)

    def __repr__(self):
        return f'ReferenceFrame(name="{self.name}")'
