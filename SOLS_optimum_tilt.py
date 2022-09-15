import numpy as np

def optimum_tilt(na, n, verbose=True):
    theta = np.arcsin(na/n)
    theta_e = np.rad2deg(
        np.arctan(np.sin(theta) / (1/(2*np.pi) + np.cos(theta))))
    theta_1 = np.rad2deg(theta)
    theta_x = theta_1 - theta_e
    theta_t = 90 - theta_e
    if verbose:
        print('Optimum tilt (NA=%0.2f, n=%0.2f):'%(na,n))
        print('theta_1=%0.2f'%theta_1)
        print('theta_e=%0.2f'%theta_e)
        print('theta_x=%0.2f'%theta_x)
        print('theta_t=%0.2f'%theta_t)
        print('')
    return theta_1, theta_e, theta_x, theta_t

if __name__ == "__main__":
    # Input:
    theta_t_135sil = optimum_tilt(1.35, 1.41)[3]
    theta_t_100wat = optimum_tilt(1.00, 1.33)[3]

    # Plot:
    na = np.linspace(0.5, 0.96, 1000)
    theta_1, theta_e, theta_x, theta_t = optimum_tilt(na, 1.00, verbose=False)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('SOLS optimum tilt')
    ax.set_ylabel('theta_t (deg)')
    ax.set_xlabel('theta_1 (deg)')
    ax.plot(theta_1, theta_t, color='g')
    ax.axvline(x=73.23, label='NA 1.35 sil (%0.2f)'%theta_t_135sil,
               linestyle='--', color='r')
    ax.axvline(x=48.75, label='NA 1.00 wat (%0.2f)'%theta_t_100wat,
               linestyle='-.', color='b')
    ax.axhline(y=55, label='AMS-AGY v2.0 max', linestyle=':', color='k')
    ax.set_ylim(ymin=0)
    plt.legend(loc="lower left")
    fig.savefig('SOLS_optimum_tilt.png', dpi=150)
    plt.show()
