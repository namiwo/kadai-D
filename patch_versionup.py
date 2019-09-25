class SemanticVersion():
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def patch_version_up(self):
        versionup_patch = self.patch + 1
        return SemanticVersion(self.major, self.minor, versionup_patch)

    def __eq__(self, other):
        if self.major == other.major and self.minor == other.minor and self.patch == other.patch:
            return True
        return False


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py371 = py370.patch_version_up()
    print(SemanticVersion(3, 7, 1) == py371)


if __name__ == "__main__":
    main()
