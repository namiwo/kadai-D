class SemanticVersion():
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def major_version_up(self):
        versionup_major = self.major + 1
        return SemanticVersion(versionup_major, 0, 0)

    def __eq__(self, other):
        if self.major == other.major and self.minor == other.minor and self.patch == other.patch:
            return True
        return False


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py400 = py370.major_version_up()
    print(SemanticVersion(4, 0, 0) == py400)


if __name__ == "__main__":
    main()
