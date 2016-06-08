! WHIZARD file utilities
!
! Automatically generated file, do not edit

module file_utils
  implicit none
  private

! Function to allow for generic I/O
! Returns the next free unit, or -1 if it fails
  public :: free_unit

  integer, parameter :: MIN_UNIT = 11, MAX_UNIT = 99

contains

  function free_unit () result (unit)
    integer :: unit
    logical :: exists, is_open
    integer :: i, status
    do i = MIN_UNIT, MAX_UNIT
       inquire (unit=i, exist=exists, opened=is_open, iostat=status)
       if (status == 0) then
          if (exists .and. .not. is_open) then
            unit = i; return
          end if
       end if
    end do
    unit = -1
  end function free_unit

end module file_utils
