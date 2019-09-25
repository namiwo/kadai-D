class SemanticVersion():
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        if (self.major == other.major and self.minor == other.minor and self.patch == other.patch):
            return True

        return False


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    print(SemanticVersion(3, 7, 0) == py370)
    print(SemanticVersion(3, 7, 1) == py370)


if __name__ == "__main__":
    main()
