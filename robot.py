import wpilib
import wpilib.drive
from ctre import WPI_TalonSRX

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        # self.gyro = wpilib.I2C(wpilib.I2C.Port.kOnboard, 0x68)
        self.leftFront = WPI_TalonSRX(5)
        self.leftBack = WPI_TalonSRX(6)
        self.rightFront = WPI_TalonSRX(7)
        self.rightBack = WPI_TalonSRX(8)
    
        self.leftDrive = wpilib.SpeedControllerGroup(self.leftBack, self.leftFront)
        self.rightDrive = wpilib.SpeedControllerGroup(self.rightBack, self.rightFront)

        self.drive = wpilib.drive.DifferentialDrive(self.leftDrive, self.rightDrive)

        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.joystick.getY(), self.joystick.getX())

if __name__ == "__main__":
    wpilib.run(Robot)