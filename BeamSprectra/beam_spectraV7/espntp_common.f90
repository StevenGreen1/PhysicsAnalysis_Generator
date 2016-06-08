module espntp_common

  use kinds, only: single

  implicit none

  real(kind=single) :: x_nm
  real(kind=single) :: y_nm
  real(kind=single) :: xp_rad
  real(kind=single) :: yp_rad

  real(kind=single) :: e1_gev
  real(kind=single) :: e2_gev
  real(kind=single) :: x_u
  real(kind=single) :: y_u
  real(kind=single) :: z_u
  real(kind=single) :: xp_urad
  real(kind=single) :: yp_urad
  common/espntp/e1_gev,e2_gev,x_u,y_u,z_u,xp_urad,yp_urad

  character(len=60), parameter ::  ch_espntp='e1_gev:R,e2_gev:R,x_u:R,y_u:R,z_u:R,xp_urad:R,yp_urad:R'
!                                             1234567890123456789012345678901234567890123456789012345

end module espntp_common




