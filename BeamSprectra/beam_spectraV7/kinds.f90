!********************************************
!* CompHEP  version  3.2    *
!********************************************
!* F90 format by Wolfgang Kilian Jul 19 1999 
!********************************************
module kinds
  implicit none
  private
 
! Three types of precision.  double is the default, usually.
  public :: single, double, quadruple
  public :: default

  integer, parameter :: single = &
       & selected_real_kind (precision(1.), range(1.))
  integer, parameter :: double = &
       & selected_real_kind (precision(1._single) + 1, range(1._single) + 1)
  integer, parameter :: quadruple = &
       & selected_real_kind (precision (1._double) + 1, range (1._double))

  integer, parameter :: default = double

end module kinds
