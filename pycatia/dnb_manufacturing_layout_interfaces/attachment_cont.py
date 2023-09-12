#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class AttachmentCont(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AttachmentCont
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement DNBIABasicDevice are ...
                | 
                | Do not use the DNBIAMRLDocAttachments interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.attachment_cont = com_object

    def get_attachment_factory(self, o_attach_factory: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAttachmentFactory(CATBaseDispatch oAttachFactory)
                | 
                |     Get the AttachmentFactory for the current document
                | 
                |     Parameters:
                | 
                |         oAttachFactory
                |             This output parameter contains the AttachmentFactory for the
                |             current document. 
                | 
                |     Returns:
                |         An HRESULT

        :param AnyObject o_attach_factory:
        :return: None
        :rtype: None
        """
        return self.attachment_cont.GetAttachmentFactory(o_attach_factory.com_object)

    def get_listof_attachments(self, o_attach_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListofAttachments(CATSafeArrayVariant oAttachList)
                | 
                |     Get list of attachments from the Attachment Container
                | 
                |     Parameters:
                | 
                |         oAttachList
                |             This output parameter contains the list of attachments in a
                |             document. 
                | 
                |     Returns:
                |         An HRESULT

        :param tuple o_attach_list:
        :return: None
        :rtype: None
        """
        return self.attachment_cont.GetListofAttachments(o_attach_list)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_listof_attachments'
        # # vba_code = """
        # # Public Function get_listof_attachments(attachment_cont)
        # #     Dim oAttachList (2)
        # #     attachment_cont.GetListofAttachments oAttachList
        # #     get_listof_attachments = oAttachList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AttachmentCont(name="{ self.name }")'
