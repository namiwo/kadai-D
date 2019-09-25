class SemanticVersion():
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def minor_version_up(self):
        versionup_minor = self.minor + 1
        return SemanticVersion(self.major, versionup_minor, self.patch)

    def __eq__(self, other):
        if self.major == other.major and self.minor == other.minor and self.patch == other.patch:
            return True
        return False


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py380 = py370.minor_version_up()
    print(SemanticVersion(3, 8, 0) == py380)


if __name__ == "__main__":
    main()
