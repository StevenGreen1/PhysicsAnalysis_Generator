module energy_spread_states

  use kinds, only: default
  use file_utils, only: free_unit

  implicit none
  private

  public :: energy_spread_state_create


  integer, parameter, public :: n_mcs_pcs_max=36

  type, public :: energy_spread_state
     character(len=200), dimension(36) :: single_file_name
     integer :: seed
     integer :: i_sqrts
     integer :: i_photon
     integer :: n_single_file
  end type energy_spread_state


  type(energy_spread_state), public :: mcs




contains


  subroutine energy_spread_state_create(energy_spread_in_name)
    character(len=*), intent(in) :: energy_spread_in_name
    integer :: iu

    mcs%single_file_name = " "
    call system_clock(mcs%seed)
    mcs%i_sqrts = 500
    mcs%i_photon = 1
    mcs%n_single_file = 0




    iu = free_unit()
    open(unit=iu, file=energy_spread_in_name, action='read', status='old')
    print *, " just opened iu,energy_spread_in_name=", iu,energy_spread_in_name
    call energy_spread_state_read_unit(iu)
    close(unit=iu)
    print "(' seed=',i12)", mcs%seed
    print "(' i_sqrts=',i12)", mcs%i_sqrts
    print "(' i_photon=',i12)", mcs%i_photon
    print "(' n_single_file=',i12)", mcs%n_single_file
    print "(' single_file_name='/(1x,a))", mcs%single_file_name(1:mcs%n_single_file)
  end subroutine energy_spread_state_create

  subroutine energy_spread_state_read_unit(u)
    integer, intent(in) :: u
     character(len=200), dimension(36) :: single_file_name
     integer :: seed
     integer :: i_sqrts
     integer :: i_photon
    namelist /energy_spread_input/ single_file_name
    namelist /energy_spread_input/ seed
    namelist /energy_spread_input/ i_sqrts
    namelist /energy_spread_input/ i_photon

    single_file_name=mcs%single_file_name
    seed=mcs%seed
    i_sqrts=mcs%i_sqrts
    i_photon=mcs%i_photon

    print *, " about to do namelist read  u=", u

    read(u, nml=energy_spread_input)

    mcs%single_file_name=single_file_name
    mcs%seed=seed
    mcs%i_sqrts=i_sqrts
    mcs%i_photon=i_photon

    mcs%n_single_file=count(mcs%single_file_name.ne." ")
    
    return

  end subroutine energy_spread_state_read_unit





end module energy_spread_states
