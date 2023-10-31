#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class SFMReferences(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SfmReferences
                | 
                | A Collection of U and V Reference elements for Standard
                | Opening.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Reference)
        self.sfm_references = com_object

    def add(self, i_reference: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Add(Reference iReference)
                | 
                |     Adds a reference in the collection.
                | 
                |     Parameters:
                | 
                |         iReference
                |             [in] Reference. 
                | 
                |     Returns:
                |         S_OK if everything ran ok. 
                |         This example Adds one U Reference to the list of
                |         SfmReferences.
                | 
                |          Dim Uref1 As Reference
                |          Set Uref1 = Part1.FindObjectByName("CROSS.95")
                |          'Add one U Reference to the list
                |          Dim UrefList As SfmReferences
                |           UrefList.Add Uref1

        :param Reference i_reference:
        :rtype: None
        """
        return self.sfm_references.Add(i_reference.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add'
        # # vba_code = """
        # # Public Function add(sfm_references)
        # #     Dim iReference (2)
        # #     sfm_references.Add iReference
        # #     add = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def clear_list(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ClearList()
                | 
                |     Clears the contents of existing list of SfmReferences.
                | 
                |     Returns:
                |         Error code
                | 
                |         Example:
                |             This example clears the contents of a list.
                | 
                |               Dim ListofRef As SfmReferences
                |               Dim Uref1 as Reference
                |               ListofRef.Add Uref1
                |               ListofRef.ClearList

        :rtype: None
        """
        return self.sfm_references.ClearList()

    def item(self, i_index: cat_variant) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Reference
                | 
                |     Retrieves a Reference from the collection of
                |     SfmReferences.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] The index of the parameter 
                |         oParm
                |             [out] The parameter 
                | 
                |     Returns:
                |         Error code
                | 
                |         Example
                |         :
                |             This example retrieves 'i'th Reference from a list of
                |             References
                | 
                |               Dim ListofRef As SfmReferences
                |               Set Ref1 = ListofRef.Item(i)

        :param cat_variant i_index:
        :rtype: Reference
        """
        return Reference(self.sfm_references.Item(i_index))

    def __repr__(self):
        return f'SFMReferences(name="{self.name}")'
