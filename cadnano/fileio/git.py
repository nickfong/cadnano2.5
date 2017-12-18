import os

import git


class GitHelper:
    """
    A wrapper class to further abstract GitPython's functionality and add
    functionality that is not natively included in GitPython.

    Each GitHelper object is used with one repository (i.e. separate GitPython
    objects are needed should one want to interact with multiple repositories.
    """
    def __init__(self, git_path):
        try:
            self._repository = git.Repo(git_path)
        except git.exc.InvalidGitRepositoryError:
            self._repository = git.Repo.init(git_path)

        self._git = self._repository.git

    def isRepoDirty(self):
        return self._repository.is_dirty()

    def checkoutBranch(self, branch_name):
        """
        Switch to a branch.

        Assumes that the specified branch name exists.

        Args:
            branch_name (str):  the name of the branch that we want to check out

        Returns:
            None
        """
        assert branch_name in self.getBranches()
        self._git.checkout(branch_name)
        assert self.getCurrentBranch() == branch_name

    def checkout(self, rev):
        """
        Switch to any git commit object.

        Assumes that the object that's associated with rev exists.

        TODO:  Assert that the rev actually exists
        TODO:  Check that we actually switched to the correct rev

        Args:
            rev (str):  the rev that we want to check out to

        Returns:
            None
        """
        assert isinstance(rev, str)

        self._git.checkout(str)

    def getBranches(self):
        """
        Get a list of this repository's local branches.

        Since `git branch --list` returns a formatted string, run the output of
        this command through parsing logic and remove the leading two spaces
        ('  ') or asterisk and space ('* '), the latter of which denotes the
        current branch.

        Returns:
            A list of this repository's local branches.
        """
        branch_string = self._git.branch('--list')
        branches = self._parseNewlines(branch_string)

        # Remove the leading two spaces or asterisk and space
        return [branch[2:] if branch[0:2] in ('  ', '* ') else branch for branch in branches]

    def newBranch(self, branch_name):
        """
        Create a new branch.

        This method assumes that branch_name is not already taken.

        Args:
            branch_name (str):  the name of the branch we want to create

        Returns:
            None
        """
        assert isinstance(branch_name, str)
        assert branch_name not in self.getBranches()

        self._git.checkout('-b', branch_name)

        assert branch_name in self.getBranches()
        assert self.getCurrentBranch() == branch_name

    def getCurrentBranch(self):
        """
        Get the current branch.

        Returns:
            The name of the current branch.
        """
        return self._repository.active_branch.name

    def add(self, filename_list):
        """
        Stage the specified files.

        Assumes that each of the specified files exists.

        TODO:  Verify that the specified files exist

        Args:
            filename_list (list):  a list of files that should be staged

        Returns:
            None
        """
        self._repository.add(filename_list)

    def commit(self, message):
        """
        Commit the staged changes.

        Assumes that changes have been staged already.

        TODO:  Ensure that changes have been staged
        TODO:  Add support for signing commits

        Args:
            message (str):  the commit message

        Returns:
            The GitPython Commit object that was created
        """
        self._repository.commit(message)
        return self._repository.commit()

    def commitAll(self, message):
        """
        Commit all tracked files that have changes.

        Args:
            message (str):  the commit message

        Returns:
            The GitPython Commit object that was created
        """
        self._git.add(update=True)
        self.commit(message)
        return self._repository.commit()

    def getCommitList(self, rev=None, skip=0, pagesize=50):
        """
        Get a list of the most recent commits.

        Args:
            rev (str):  the git object that we should start from
            skip (int):  the number of commits that we should skip before
                starting to return commits
            pagesize (int):  the number of commits that should be returned

        Returns:
            A list of GitPython Commit objects
        """
        if rev:
            return list(self._repository.iter_commits(rev, max_count=pagesize, skip=skip))
        else:
            return list(self._repository.iter_commits(max_count=pagesize, skip=skip))

    def getCommitIterator(self, rev):
        """
        Get an iterator that iterates over the most recent commits starting from
        rev.

        Returns:
            An iterator that returns GitPython Commit objects
        """
        raise NotImplementedError

    def addRemote(self, name, uri):
        """
        Add a new remote.

        Assumes that the name of the remote is not already taken.

        Args:
            name (str):  the name of the remote to be created
            uri (str):  the URI of the remote

        Returns:
            None
        """
        assert isinstance(name, str) and len(name)
        assert isinstance(uri, str) and len(uri)

        assert name not in self.getRemotes()
        self._git.remote('add', name, uri)
        assert name in self.getRemotes()

    def removeRemote(self, name):
        """
        Remove a new remote.

        Assumes that the remote exists.

        Args:
            name (str):  the name of the remote to be created

        Returns:
            None
        """
        assert isinstance(name, str) and len(name)

        assert name in self.getRemotes()
        self._git.remote('remove', name)
        assert name not in self.getRemotes()

    def getRemotes(self):
        """
        Get a list of remotes.

        Returns:
            A list of remotes
        """
        remotes = self._git.remote()
        return self._parseNewlines(remotes)

    def push(self, remote, branch=None):
        """
        Push local commits to the specified remote.

        Assumes that keyboard-interactive authentication is not needed.

        TODO:  Support keyboard-interactive authentication, SSH keys with
        passphrases, and GitHub/GitLab/BitBucket integration

        Args:
            remote (str):  the remote we want to push to
            branch (str):  the branch we want to push to

        Returns:
            The STDOUT from pushing
        """
        assert isinstance(remote, str)
        assert remote in self.getRemotes()
        if branch is not None:
            assert isinstance(branch, str)
            assert branch in self.getBranches()

        stdout = self._git.push(remote, branch if branch else self.getCurrentBranch())
        return stdout

    def pull(self, remote, branch=None):
        """
        Pull local commits from the specified remote.

        Assumes that keyboard-interactive authentication is not needed.

        TODO:  Support keyboard-interactive authentication, SSH keys with
        passphrases, and GitHub/GitLab/BitBucket integration

        Args:
            remote (str):  the remote we want to pull from
            branch (str):  the branch we want to pull from

        Returns:
            The STDOUT from pulling
        """
        assert isinstance(remote, str)
        assert remote in self.getRemotes()
        if branch is not None:
            assert isinstance(branch, str)
            assert branch in self.getBranches()

        stdout = self._git.pull(remote, branch if branch else self.getCurrentBranch())
        return stdout

    def _parseGitOutput(self, stdout):
        """
        Parse output from git commands.

        Looks for newlines and tabs.

        Args:
            stdout (str):  the string to be parsed

        Returns:
            A 2-deep nested list where each column of output is separated in the
                inner list and each row of output is separated in the outer list

        """
        assert isinstance(stdout, str)

        raw_lines = self._parseNewlines(stdout)
        tabbed_lines = [self._parseTabs(line) for line in raw_lines]

        return tabbed_lines

    @staticmethod
    def _parseNewlines(stdout):
        """
        Given a string split on the host OS' newline character.

        Args:
            stdout (str):  the string to be parsed

        Returns:
            A list corresponding to the input string split on the OS' newline character
        """
        assert isinstance(stdout, str)
        return stdout.split(os.linesep)

    @staticmethod
    def _parseTabs(stdout):
        """
        Given a string split on tab characters.

        Args:
            stdout (str):  the string to be parsed

        Returns:
            A list corresponding to the input string split on tabs
        """
        assert isinstance(stdout, str)
        return stdout.split('\t')


class CommitIterator:
    def __init__(self, repo, start):
        assert isinstance(repo, git.Repo)
        assert isinstance(start, int)

        self.location = start
        self.repo = repo

    def __iter__(self):
        return self

    def next(self):
        pass
