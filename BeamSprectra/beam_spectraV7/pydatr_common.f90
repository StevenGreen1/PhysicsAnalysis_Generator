module pydatr_common

  use kinds, only: double 

  implicit none

  integer, dimension(6) :: mrpy
  real(kind=double), dimension(100) :: rrpy
  common/pydatr/mrpy,rrpy


end module pydatr_common




