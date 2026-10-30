import time
import random
from datetime import datetime


class APTSimulation:
    def __init__(self, target):
        self.target = target
        self.logs = []
        self.status = "Initialized"

    def log_event(self, stage, action, severity="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        event = {
            "timestamp": timestamp,
            "stage": stage,
            "action": action,
            "severity": severity
        }

        self.logs.append(event)

        print(
            f"[{timestamp}] "
            f"[{severity}] "
            f"{stage}: {action}"
        )

        time.sleep(1)

    # Stage 1 - Reconnaissance
    def reconnaissance(self):
        self.status = "Reconnaissance"

        self.log_event(
            "Reconnaissance",
            f"Simulating information gathering against {self.target}"
        )

        self.log_event(
            "Reconnaissance",
            "Identifying simulated users and services"
        )

    # Stage 2 - Initial Access
    def initial_access(self):
        self.status = "Initial Access"

        self.log_event(
            "Initial Access",
            "Simulating delivery of a malicious document",
            "WARNING"
        )

        self.log_event(
            "Initial Access",
            "User interaction detected in simulation",
            "WARNING"
        )

    # Stage 3 - Execution
    def execution(self):
        self.status = "Execution"

        self.log_event(
            "Execution",
            "Simulating execution of attacker-controlled code",
            "HIGH"
        )

        self.log_event(
            "Execution",
            "Payload execution completed in isolated simulation",
            "HIGH"
        )

    # Stage 4 - Persistence
    def persistence(self):
        self.status = "Persistence"

        self.log_event(
            "Persistence",
            "Simulating creation of a persistence mechanism",
            "HIGH"
        )

        self.log_event(
            "Persistence",
            "Persistence mechanism recorded for detection testing",
            "HIGH"
        )

    # Stage 5 - Privilege Escalation
    def privilege_escalation(self):
        self.status = "Privilege Escalation"

        self.log_event(
            "Privilege Escalation",
            "Simulating attempt to obtain higher privileges",
            "HIGH"
        )

        success = random.choice([True, False])

        if success:
            self.log_event(
                "Privilege Escalation",
                "Simulated privilege escalation succeeded",
                "CRITICAL"
            )
        else:
            self.log_event(
                "Privilege Escalation",
                "Simulated privilege escalation failed",
                "WARNING"
            )

    # Stage 6 - Discovery
    def discovery(self):
        self.status = "Discovery"

        self.log_event(
            "Discovery",
            "Simulating system information discovery"
        )

        self.log_event(
            "Discovery",
            "Simulating account and service discovery"
        )

        self.log_event(
            "Discovery",
            "Simulating network environment discovery"
        )

    # Stage 7 - Command and Control
    def command_control(self):
        self.status = "Command and Control"

        self.log_event(
            "Command & Control",
            "Simulating communication with a fake C2 server",
            "HIGH"
        )

        self.log_event(
            "Command & Control",
            "No real network connection was established"
        )

    # Stage 8 - Data Collection
    def collection(self):
        self.status = "Collection"

        self.log_event(
            "Collection",
            "Simulating collection of test data",
            "WARNING"
        )

        self.log_event(
            "Collection",
            "Test data staged inside the simulation"
        )

    # Stage 9 - Exfiltration
    def exfiltration(self):
        self.status = "Exfiltration"

        self.log_event(
            "Exfiltration",
            "Simulating attempted data transfer",
            "CRITICAL"
        )

        self.log_event(
            "Exfiltration",
            "Data transfer blocked — simulation only",
            "INFO"
        )

    # Detection report
    def generate_report(self):
        print("\n" + "=" * 65)
        print("             APT SIMULATION REPORT")
        print("=" * 65)

        print(f"Target       : {self.target}")
        print(f"Final Status : {self.status}")
        print(f"Events       : {len(self.logs)}")

        print("\nAttack Stages:")

        stages = []

        for event in self.logs:
            if event["stage"] not in stages:
                stages.append(event["stage"])

        for number, stage in enumerate(stages, start=1):
            print(f"{number}. {stage}")

        print("\nSecurity Events:")

        for event in self.logs:
            if event["severity"] in ["HIGH", "CRITICAL"]:
                print(
                    f"- [{event['severity']}] "
                    f"{event['stage']}: "
                    f"{event['action']}"
                )

        print("=" * 65)


def main():

    print("=" * 65)
    print("          ADVANCED PERSISTENT THREAT SIMULATOR")
    print("=" * 65)

    print("\nWARNING:")
    print("This program is an offline cybersecurity simulation.")
    print("It does not exploit systems, create real persistence,")
    print("connect to C2 servers, or exfiltrate real data.\n")

    target = input("Enter simulated target name: ")

    apt = APTSimulation(target)

    # Simulated APT attack lifecycle
    apt.reconnaissance()
    apt.initial_access()
    apt.execution()
    apt.persistence()
    apt.privilege_escalation()
    apt.discovery()
    apt.command_control()
    apt.collection()
    apt.exfiltration()

    # Generate final report
    apt.generate_report()


if __name__ == "__main__":
    main()